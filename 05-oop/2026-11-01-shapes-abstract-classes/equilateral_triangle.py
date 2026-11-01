from isosceles_triangle import IsoscelesTriangle


class EquilateralTriangle(IsoscelesTriangle):
    def __init__(self, a, h):
        super().__init__(a, a, h)
