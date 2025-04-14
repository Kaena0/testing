class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

        
    def get_angles(self):
        """Повертає кількість кутів у фігури."""
        if self.type == "трикутник":
            return 3
        elif self.type == "прямокутник":
            return 4
        elif self.type == "квадрат":
            return 4
        else:
            return 0  # На всяк випадок

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.length  # тут ми вже виправляємо попередню помилку
