from random import randint


class Die():
    """Класс представляющий бросок 1-го кубика"""

    def __init__(self, numsides=6):
        """По умолчанию кубик 6и гранный"""
        self.numsides = numsides

    def roll(self):
        """Бросок кубика и выпавшая грань"""
        return randint(1, self.numsides)
