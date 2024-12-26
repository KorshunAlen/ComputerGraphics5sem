class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Настройки снарядов
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 0.2
        self.fleet_drop_speed = 8
        self.fleet_direction = 1  # 1 = вправо, -1 = влево

        # Ускорение игры
        self.speedup_scale = 1.1

    def increase_speed(self):
        """Увеличивает настройки скорости."""
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
