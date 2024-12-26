import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Размер окна
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Масштабируемый и вращающийся квадрат")

# Начальные координаты квадрата, умноженные на 100
square_points = np.array([[2, -2],
                          [-2, -2],
                          [-2, 2],
                          [2, 2]]) * 100

# Параметры трансформации
m = 0.9  # Коэффициент масштабирования
alpha = np.pi / 32  # Угол поворота

# Функция для поворота точки на угол
def rotate_point(x, y, angle):
    cos_angle = np.cos(angle)
    sin_angle = np.sin(angle)
    x_new = cos_angle * x - sin_angle * y
    y_new = sin_angle * x + cos_angle * y
    return x_new, y_new

# Функция для масштабирования точки
def scale_point(x, y, scale_factor):
    return x * scale_factor, y * scale_factor

# Функция для рисования квадрата
def draw_square(points):
    pygame.draw.polygon(screen, (0, 0, 255), points, 1)

# Основной цикл
running = True
for i in range(20):
    screen.fill((255, 255, 255))  # Заполняем фон

    # Масштабирование
    scaled_points = [scale_point(x, y, m) for x, y in square_points]

    # Поворот
    rotated_points = [rotate_point(x, y, alpha) for x, y in scaled_points]

    # Смещение квадрата в центр экрана
    offset_x, offset_y = screen_width // 2, screen_height // 2
    translated_points = [(x + offset_x, y + offset_y) for x, y in rotated_points]

    # Отрисовка квадрата
    draw_square(translated_points)

    # Обновление экрана
    pygame.display.flip()

    # Задержка для визуализации
    pygame.time.delay(200)

    # Обработка событий для закрытия окна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

# Закрытие pygame
pygame.quit()
