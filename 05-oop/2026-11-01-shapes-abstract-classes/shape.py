from abc import ABC, abstractmethod


# ABC מאפשרת להגדיר מחלקת בסיס מופשטת.
class Shape(ABC):
    def __init__(self, name):
        self._name = name

    # property מאפשרת קריאה ללא סוגריים; ללא setter אי אפשר להציב בה ערך.
    @property
    def name(self):
        return self._name

    # abstractmethod מחייבת מימוש במחלקה קונקרטית; property נכתבת מעליה.
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass
