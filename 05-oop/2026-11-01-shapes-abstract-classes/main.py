import math

from circle import Circle
from equilateral_triangle import EquilateralTriangle
from isosceles_triangle import IsoscelesTriangle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


def main():
    shapes = [
        Rectangle(3, 4),
        Square(4),
        Circle(2),
        Triangle(3, 4, 5, 4),  # משולש ישר זווית: הבסיס 3 והגובה 4.
        IsoscelesTriangle(6, 5, 4),  # חצי בסיס 3, גובה 4 ושוק 5.
        EquilateralTriangle(4, 2 * math.sqrt(3)),
    ]

    # פולימורפיזם: אותה גישה לתכונות מפעילה את החישוב המתאים לכל אובייקט.
    for shape in shapes:
        print(f"{shape.name}: area={shape.area:.2f}, perimeter={shape.perimeter:.2f}")


if __name__ == "__main__":
    main()
