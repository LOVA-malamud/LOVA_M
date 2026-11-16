from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, a):
        # שתי צלעות שוות מאפשרות שימוש בנוסחאות המלבן ללא שינוי.
        super().__init__(a, a)
