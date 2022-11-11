from random import choice  # choice используется для выбора случайного элемента из списка


class RandomWalk():
    """класс для генерирования случайных блужданий"""

    def __init__(self, num_points=5000):
        """инициализирует атрибуты блужданий"""
        self.num_points = num_points

        """Все блуждания начинаются с (0, 0)"""
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """Вычисляет все точки блуждания"""
        # определение направления и длинны перемещения
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        # Шаги генерируются до достижения нужной длинны
        while len(self.x_values) < self.num_points:

            x_step = self.get_step()
            y_step = self.get_step()

            # Отклонение нулевых перемещений
            if x_step == 0 and y_step == 0:
                continue

            # Вычисление следующих значений Х и У
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)