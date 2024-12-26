import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Размер окна
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Преобразование отрезков")

# Исходные координаты
x1, y1 = 0, 100
x2, y2 = 200, 300

# Матрица преобразования
T = np.array([[1, 2], [3, 1]])

# Функция для преобразования точки с помощью матрицы
def transform_point(x, y, T):
    point = np.array([x, y])
    transformed_point = np.dot(T, point)
    return transformed_point[0], transformed_point[1]

# Преобразуем обе точки
x1_prime, y1_prime = transform_point(x1, y1, T)
x2_prime, y2_prime = transform_point(x2, y2, T)

# Середины отрезков
midpoint_original = ((x1 + x2) / 2, (y1 + y2) / 2)
midpoint_transformed = ((x1_prime + x2_prime) / 2, (y1_prime + y2_prime) / 2)

# Настройки отображения
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CIRCLE_RADIUS = 5

# Масштабирование (коэффициент для отображения)
scale = 0.1  # уменьшить для более плотного отображения

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона
    screen.fill(WHITE)

    # Рисуем исходный отрезок (красный) с масштабированием
    pygame.draw.line(screen, RED,
                     (int(x1 * scale), int(y1 * scale)),
                     (int(x2 * scale), int(y2 * scale)), 2)

    # Рисуем преобразованный отрезок (синий) с масштабированием
    pygame.draw.line(screen, BLUE,
                     (int(x1_prime * scale), int(y1_prime * scale)),
                     (int(x2_prime * scale), int(y2_prime * scale)), 2)

    # Рисуем середины исходного и преобразованного отрезков (зеленые) с масштабированием
    pygame.draw.circle(screen, GREEN,
                       (int(midpoint_original[0] * scale), int(midpoint_original[1] * scale)),
                       CIRCLE_RADIUS)
    pygame.draw.circle(screen, GREEN,
                       (int(midpoint_transformed[0] * scale), int(midpoint_transformed[1] * scale)),
                       CIRCLE_RADIUS)

    # Соединяем середины отрезков
    pygame.draw.line(screen, (0, 0, 0),
                     (int(midpoint_original[0] * scale), int(midpoint_original[1] * scale)),
                     (int(midpoint_transformed[0] * scale), int(midpoint_transformed[1] * scale)), 2)

    # Обновляем экран
    pygame.display.flip()

# Закрытие pygame
pygame.quit()
