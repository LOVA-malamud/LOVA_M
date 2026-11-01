from four_side import FourSide


class Rectangle(FourSide):
    def __init__(self, a, b):
        # super מאתחלת את חלק ההורה באותו אובייקט; האתחול מגיע ל־Shape.
        super().__init__("Rectangle")
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)
