import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task 3: Line Transformation")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Матрица преобразования
T = np.array([
    [1, 3],
    [4, 1]
])

# Функция для преобразования координат
def transform_segment(segment, matrix):
    return np.dot(matrix, segment.T).T

# Главная функция
def main():
    # Исходные координаты отрезка (две точки)
    segment = np.array([
        [100, 200],  # Точка 1
        [300, 400]   # Точка 2
    ])

    # Преобразованный отрезок
    transformed_segment = transform_segment(segment, T)

    # Вывод координат в консоль
    print(f"Исходные координаты отрезка: {segment}")
    print(f"Преобразованные координаты отрезка: {transformed_segment}")

    # Центр окна для удобства отображения
    center = np.array([WIDTH // 2, HEIGHT // 2])

    # Координаты для рисования с учетом центра окна и масштабирования
    scale = 0.5  # Масштаб уменьшен для корректного отображения
    segment_draw = center + segment * scale
    transformed_draw = center + transformed_segment * scale

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовка
        WINDOW.fill(WHITE)

        # Отображение исходного отрезка
        pygame.draw.line(WINDOW, RED, segment_draw[0].astype(int), segment_draw[1].astype(int), 3)

        # Отображение преобразованного отрезка
        pygame.draw.line(WINDOW, BLUE, transformed_draw[0].astype(int), transformed_draw[1].astype(int), 3)

        # Обновление окна
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
