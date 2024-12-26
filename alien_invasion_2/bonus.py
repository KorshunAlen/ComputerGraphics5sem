import pygame
from pygame.sprite import Sprite


class Bonus(Sprite):
    """Класс для бонусов."""

    def __init__(self, ai_game, bonus_type):
        """Инициализирует бонус и задаёт его тип и начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        self.type = bonus_type

        self.image = pygame.image.load(f'images/shield.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)
        self.speed = 0.5

    def update(self):
        """Перемещает бонус вниз по экрану."""
        self.y += self.speed
        self.rect.y = self.y

    def draw_bonus(self):
        """Рисует бонус на экране."""
        self.screen.blit(self.image, self.rect)
