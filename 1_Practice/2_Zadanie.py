import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task 2: Draw Primitives")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Главная функция
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовка
        WINDOW.fill(WHITE)

        # Примитивы
        # 1. Линии
        pygame.draw.line(WINDOW, RED, (50, 50), (550, 50), 5)  # Верхняя линия
        pygame.draw.line(WINDOW, GREEN, (50, 50), (50, 550), 5)  # Левая линия
        pygame.draw.line(WINDOW, BLUE, (550, 50), (550, 550), 5)  # Правая линия
        pygame.draw.line(WINDOW, YELLOW, (50, 550), (550, 550), 5)  # Нижняя линия

        # 2. Окружность
        pygame.draw.circle(WINDOW, BLUE, (300, 300), 100, 5)  # Центральная окружность

        # 3. Текст
        font = pygame.font.Font(None, 36)
        text = font.render("Примитивы Pygame", True, BLACK)
        WINDOW.blit(text, (200, 20))

        # Обновление окна
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
