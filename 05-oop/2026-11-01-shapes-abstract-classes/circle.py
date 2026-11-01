import math

from shape import Shape


class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle")
        self._r = r

    @property
    def r(self):
        return self._r

    @property
    def area(self):
        return math.pi * self.r ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.r
