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

        # Настройки снарядов
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 0.3
        self.fleet_drop_speed = 2
        self.fleet_direction = 1  # 1 = вправо, -1 = влево
