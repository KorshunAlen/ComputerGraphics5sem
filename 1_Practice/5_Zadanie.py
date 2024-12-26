import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Размер окна
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Преобразование отрезков и наклоны")

# Исходные координаты для двух параллельных отрезков
x1, y1 = 50, 100
x2, y2 = 250, 200
x3, y3 = 50, 200
x4, y4 = 250, 300

# Матрица преобразования
T = np.array([[1, 2], [3, 1]])

# Функция для преобразования точки с помощью матрицы
def transform_point(x, y, T):
    point = np.array([x, y])
    transformed_point = np.dot(T, point)
    return transformed_point[0], transformed_point[1]

# Преобразуем точки отрезков
x1_prime, y1_prime = transform_point(x1, y1, T)
x2_prime, y2_prime = transform_point(x2, y2, T)
x3_prime, y3_prime = transform_point(x3, y3, T)
x4_prime, y4_prime = transform_point(x4, y4, T)

# Функция для вычисления наклона отрезка
def calculate_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

# Наклоны исходных и преобразованных отрезков
slope_original_1 = calculate_slope(x1, y1, x2, y2)
slope_original_2 = calculate_slope(x3, y3, x4, y4)
slope_transformed_1 = calculate_slope(x1_prime, y1_prime, x2_prime, y2_prime)
slope_transformed_2 = calculate_slope(x3_prime, y3_prime, x4_prime, y4_prime)

# Настройки отображения
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
CIRCLE_RADIUS = 5
BLACK = (0, 0, 0)

# Масштабирование для отображения в окне
scale = 0.1  # масштаб

# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заполнение фона
    screen.fill(WHITE)

    # Рисуем исходные отрезки (красный)
    pygame.draw.line(screen, RED,
                     (int(x1 * scale), int(y1 * scale)),
                     (int(x2 * scale), int(y2 * scale)), 2)
    pygame.draw.line(screen, RED,
                     (int(x3 * scale), int(y3 * scale)),
                     (int(x4 * scale), int(y4 * scale)), 2)

    # Рисуем преобразованные отрезки (синий)
    pygame.draw.line(screen, BLUE,
                     (int(x1_prime * scale), int(y1_prime * scale)),
                     (int(x2_prime * scale), int(y2_prime * scale)), 2)
    pygame.draw.line(screen, BLUE,
                     (int(x3_prime * scale), int(y3_prime * scale)),
                     (int(x4_prime * scale), int(y4_prime * scale)), 2)

    # Рисуем наклоны в тексте
    font = pygame.font.SysFont(None, 24)
    text_original_1 = font.render(f"Наклон 1: {slope_original_1:.2f}", True, BLACK)
    text_original_2 = font.render(f"Наклон 2: {slope_original_2:.2f}", True, BLACK)
    text_transformed_1 = font.render(f"Наклон 1 (преобраз.): {slope_transformed_1:.2f}", True, BLACK)
    text_transformed_2 = font.render(f"Наклон 2 (преобраз.): {slope_transformed_2:.2f}", True, BLACK)

    # Размещаем текст внизу экрана, чтобы не было пересечений
    screen.blit(text_original_1, (10, screen_height - 100))
    screen.blit(text_original_2, (10, screen_height - 80))
    screen.blit(text_transformed_1, (10, screen_height - 60))
    screen.blit(text_transformed_2, (10, screen_height - 40))

    # Обновляем экран
    pygame.display.flip()

# Закрытие pygame
pygame.quit()
