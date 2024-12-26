import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Task 1: Point Transformation")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Матрица преобразования
T = np.array([
    [1, 3],
    [4, 1]
])


# Функция для преобразования координат
def transform_point(point, matrix):
    vector = np.array(point)
    return np.dot(matrix, vector)


# Функция для получения ввода координат от пользователя
def get_user_input():
    print("Введите координаты точки (x и y) через пробел: ")
    while True:
        try:
            user_input = input().strip()
            x, y = map(float, user_input.split())
            return np.array([x, y])
        except ValueError:
            print("Ошибка ввода. Пожалуйста, введите два числа, разделённых пробелом: ")


# Главная функция
def main():
    # Ввод координат точки
    original_point = get_user_input()

    # Преобразование точки
    transformed_point = transform_point(original_point, T)

    # Вывод координат в консоль
    print(f"Исходные координаты: {original_point}")
    print(f"Преобразованные координаты: {transformed_point}")

    # Центр окна для удобства отображения
    center = np.array([WIDTH // 2, HEIGHT // 2])

    # Координаты для рисования с учетом центра окна и масштабирования
    scale = 1  # Масштаб (можно изменить, если точки выходят за пределы экрана)
    original_draw = center + original_point * scale
    transformed_draw = center + transformed_point * scale

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Отрисовка
        WINDOW.fill(WHITE)

        # Отображение исходной точки
        pygame.draw.circle(WINDOW, RED, original_draw.astype(int), 5)
        pygame.draw.line(WINDOW, (0, 0, 0), center, original_draw.astype(int), 1)

        # Отображение преобразованной точки
        pygame.draw.circle(WINDOW, BLUE, transformed_draw.astype(int), 5)
        pygame.draw.line(WINDOW, (0, 0, 0), center, transformed_draw.astype(int), 1)

        # Обновление окна
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
