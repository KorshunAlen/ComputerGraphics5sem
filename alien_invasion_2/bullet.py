import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления снарядами."""

    def __init__(self, ai_game, powered_up=False):
        """Создаёт объект снаряда в текущей позиции корабля."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)
        self.powered_up = powered_up  # Усиленный снаряд

    def update(self):
        """Перемещает снаряд вверх по экрану."""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисует снаряд на экране."""
        pygame.draw.rect(self.screen, self.color, self.rect)
