import pygame
import numpy as np

# Инициализация pygame
pygame.init()

# Размер окна
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Преобразование пересекающихся отрезков")

# Исходные координаты для отрезков (умножены на 100 для увеличения длины)
L = np.array([
    [-1/2, 3/2],
    [3, -2],
    [-1, -1],
    [3, 5/3]
])

# Матрица преобразования
T = np.array([[1, 2], [1, -3]])

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

# Настройки отображения
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CIRCLE_RADIUS = 5
BLACK = (0, 0, 0)

# Масштабирование для отображения в окне
scale = 1  # Масштаб не меняем, так как уже умножили на 100

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
                     (int(L_scaled[0, 0] * scale), int(L_scaled[0, 1] * scale)),
                     (int(L_scaled[1, 0] * scale), int(L_scaled[1, 1] * scale)), 2)
    pygame.draw.line(screen, RED,
                     (int(L_scaled[2, 0] * scale), int(L_scaled[2, 1] * scale)),
                     (int(L_scaled[3, 0] * scale), int(L_scaled[3, 1] * scale)), 2)

    # Рисуем преобразованные отрезки (синий)
    pygame.draw.line(screen, BLUE,
                     (int(L_transformed[0, 0] * scale), int(L_transformed[0, 1] * scale)),
                     (int(L_transformed[1, 0] * scale), int(L_transformed[1, 1] * scale)), 2)
    pygame.draw.line(screen, BLUE,
                     (int(L_transformed[2, 0] * scale), int(L_transformed[2, 1] * scale)),
                     (int(L_transformed[3, 0] * scale), int(L_transformed[3, 1] * scale)), 2)

    # Обновляем экран
    pygame.display.flip()

# Закрытие pygame
pygame.quit()
