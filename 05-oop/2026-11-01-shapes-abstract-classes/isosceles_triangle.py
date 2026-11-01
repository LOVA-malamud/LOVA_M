from triangle import Triangle


class IsoscelesTriangle(Triangle):
    def __init__(self, a, c, h):
        super().__init__(a, c, c, h)
