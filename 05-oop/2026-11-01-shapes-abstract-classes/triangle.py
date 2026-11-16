from shape import Shape


class Triangle(Shape):
    def __init__(self, a, b, c, h):
        super().__init__("Triangle")
        self._a = a
        self._b = b
        self._c = c
        self._h = h

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def c(self):
        return self._c

    @property
    def h(self):
        return self._h

    @property
    def area(self):
        # h הוא הגובה המאונך לצלע a.
        return self.a * self.h / 2

    @property
    def perimeter(self):
        return self.a + self.b + self.c
