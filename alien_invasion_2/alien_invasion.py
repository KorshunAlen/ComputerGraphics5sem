import sys
import pygame
import pickle
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from bonus import Bonus
import pygame.mixer

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        # Настройки экрана
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Инициализация ресурсов
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.bonuses = pygame.sprite.Group()

        self.level = 1
        self.lives = 3
        self.score = 0

        self._create_fleet()

        # Инициализация звуков
        self.laser_sound = pygame.mixer.Sound("sounds/laser.wav")
        self.explosion_sound = pygame.mixer.Sound("sounds/alien_explosion.wav")
        self.life_lost_sound = pygame.mixer.Sound("sounds/lose_life.wav")
        self.game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")

        # Флаги для усилений
        self.shield_active = False
        self.shield_timer = 0
        self.bullet_power = False
        self.power_timer = 0

    def run_game(self):
        """Запускает основной цикл игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_s:
            self._save_game()
        elif event.key == pygame.K_l:
            self._load_game()

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создаёт новый снаряд и добавляет его в группу bullets."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.bullet_power)
            self.bullets.add(new_bullet)
            self.laser_sound.play()

    def _update_bullets(self):
        """Обновляет позиции снарядов и удаляет старые."""
        self.bullets.update()

        # Удаление снарядов, вышедших за экран.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Обрабатывает столкновения снарядов с пришельцами."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            self.explosion_sound.play()
            self.score += 10 * len(collisions)

        if not self.aliens:
            # Переход на следующий уровень
            self.bullets.empty()
            self.level += 1
            self.settings.increase_speed()
            self._create_fleet()

    def _create_fleet(self):
        """Создаёт флот пришельцев."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Создаёт пришельца и размещает его в ряду."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Проверяет, достиг ли флот края экрана, затем обновляет позиции всех пришельцев."""
        self._check_fleet_edges()
        self.aliens.update()

        # Проверка столкновения пришельцев с кораблём
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if not self.shield_active:
            self.lives -= 1
            self.life_lost_sound.play()

        if self.lives <= 0:
            self.game_over_sound.play()
            sys.exit()

        # Удаление пришельцев и снарядов, восстановление флота
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()

        # Перемещение корабля в центр
        self.ship.center_ship()

    def _save_game(self):
        """Сохраняет текущий прогресс игры."""
        game_data = {
            "level": self.level,
            "score": self.score,
            "lives": self.lives
        }
        with open("savefile.pkl", "wb") as f:
            pickle.dump(game_data, f)

    def _load_game(self):
        """Загружает прогресс игры."""
        try:
            with open("savefile.pkl", "rb") as f:
                game_data = pickle.load(f)
                self.level = game_data["level"]
                self.score = game_data["score"]
                self.lives = game_data["lives"]
        except FileNotFoundError:
            print("Сохранение не найдено.")

    def _update_screen(self):
        """Обновляет изображения на экране и переключает на новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        for bonus in self.bonuses:
            bonus.draw_bonus()

        pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
