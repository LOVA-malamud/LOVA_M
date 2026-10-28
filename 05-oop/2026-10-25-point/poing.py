
class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def X(self):
        return self._x

    @property
    def Y(self):
        return self._y


point1 = Point(9.44, -10)

print(point1.X)
print(point1.Y)
