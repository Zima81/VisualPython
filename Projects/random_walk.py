from random import choice  # choice используется для выбора случайного элемента из списка


class RandomWalk():
    """класс для генерирования случайных блужданий"""

    def __init__(self, num_points=5000):
        """инициализирует атрибуты блужданий"""
        self.num_points = num_points

        """Все блуждания начинаются с (0, 0)"""
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания"""

        # Шаги генерируются до достижения нужной длинны
        while len(self.x_values) < self.num_points:

            # определение нароаления и длинны перемещения
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений Х и У
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
