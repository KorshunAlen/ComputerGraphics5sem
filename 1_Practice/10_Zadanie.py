import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Размер начального окна
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Спираль Паскаля")

# Параметры спирали
a = 1  # Константа для амплитуды
b = 100  # Константа для сдвига
theta_max = 10 * np.pi  # Максимальный угол (для нескольких витков)

# Функция для вычисления полярных координат и преобразования в декартовы
def polar_to_cartesian(theta, a, b):
    r = b + 2 * a * theta  # Радиус растет с углом
    x = r * np.cos(theta)  # Преобразуем в декартовы координаты
    y = r * np.sin(theta)
    return x, y

# Масштабирование координат для корректного отображения в окне
def scale_coordinates(x, y, width, height, scale_factor=1):
    # Центрируем спираль в центре экрана
    x_scaled = int(width / 2 + x * scale_factor)
    y_scaled = int(height / 2 - y * scale_factor)
    return x_scaled, y_scaled

# Основной цикл
running = True
points = []  # Список для хранения точек спирали

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Вычисляем координаты для разных значений угла
    points.clear()  # Очищаем список точек на каждом кадре
    for theta in np.linspace(0, theta_max, 1000):  # Разбиваем угол на 1000 шагов
        x, y = polar_to_cartesian(theta, a, b)
        x_scaled, y_scaled = scale_coordinates(x, y, screen_width, screen_height, scale_factor=0.5)
        points.append((x_scaled, y_scaled))

    # Заполнение фона
    screen.fill((255, 255, 255))

    # Рисуем спираль, соединяя последовательные точки
    pygame.draw.lines(screen, (0, 0, 255), False, points, 1)

    # Обновляем экран
    pygame.display.flip()

# Закрытие pygame
pygame.quit()

