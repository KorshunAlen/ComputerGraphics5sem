import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Размер начального окна
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Масштабирование треугольника")

# Исходные координаты для треугольника (умножены на 100 для увеличения длины)
L = np.array([
    [5, 1],
    [5, 2],
    [3, 2]
])

# Матрица масштабирования на 2 (увеличиваем в 2 раза)
T = np.array([[2, 0], [0, 2]])


# Функция для преобразования точки с помощью матрицы
def transform_point(x, y, T):
    point = np.array([x, y])
    transformed_point = np.dot(T, point)
    return transformed_point[0], transformed_point[1]


# Умножаем исходные точки на 100 для увеличения длины
L_scaled = L * 100

# Преобразуем все точки с помощью матрицы T
L_transformed = np.array([transform_point(x, y, T) for x, y in L_scaled])

# Сдвиг отрезков в видимую область (для сдвига добавим константу)
shift_x, shift_y = 400, 400  # Сдвиг в центр окна
L_transformed += np.array([shift_x, shift_y])
L_scaled += np.array([shift_x, shift_y])


# Функция для получения масштаба относительно размеров экрана
def get_scale_factor(screen_width, screen_height, L_scaled, L_transformed):
    # Найдем минимальные и максимальные значения координат для исходного и преобразованного треугольников
    min_x = min(np.min(L_scaled[:, 0]), np.min(L_transformed[:, 0]))
    max_x = max(np.max(L_scaled[:, 0]), np.max(L_transformed[:, 0]))
    min_y = min(np.min(L_scaled[:, 1]), np.min(L_transformed[:, 1]))
    max_y = max(np.max(L_scaled[:, 1]), np.max(L_transformed[:, 1]))

    # Определим размеры, которые должны быть видны
    width = max_x - min_x
    height = max_y - min_y

    # Рассчитаем коэффициент масштаба так, чтобы треугольники помещались в окно
    scale_x = screen_width / width
    scale_y = screen_height / height
    scale_factor = min(scale_x, scale_y)

    return scale_factor, min_x, min_y


# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем масштабный коэффициент и обновляем размеры
    scale_factor, min_x, min_y = get_scale_factor(screen.get_width(), screen.get_height(), L_scaled, L_transformed)

    # Заполнение фона
    screen.fill((255, 255, 255))

    # Рисуем исходный треугольник (красный)
    pygame.draw.polygon(screen, (255, 0, 0), [
        (int((L_scaled[0, 0] - min_x) * scale_factor), int((L_scaled[0, 1] - min_y) * scale_factor)),
        (int((L_scaled[1, 0] - min_x) * scale_factor), int((L_scaled[1, 1] - min_y) * scale_factor)),
        (int((L_scaled[2, 0] - min_x) * scale_factor), int((L_scaled[2, 1] - min_y) * scale_factor))
    ], 2)

    # Рисуем преобразованный треугольник (синий)
    pygame.draw.polygon(screen, (0, 0, 255), [
        (int((L_transformed[0, 0] - min_x) * scale_factor), int((L_transformed[0, 1] - min_y) * scale_factor)),
        (int((L_transformed[1, 0] - min_x) * scale_factor), int((L_transformed[1, 1] - min_y) * scale_factor)),
        (int((L_transformed[2, 0] - min_x) * scale_factor), int((L_transformed[2, 1] - min_y) * scale_factor))
    ], 2)

    # Обновляем экран
    pygame.display.flip()

# Закрытие pygame
pygame.quit()
