# TODO: описать базовый класс
class ConiferousTree:
    """
        Базовый класс ConiferousTree.

        Атрибуты:
            age (int): Возраст дерева.
            height (float): Высота дерева в метрах

        Методы:
            init: Конструктор для инициализации объекта.
            str: Возвращает строковое представление объекта.
            repr: Возвращает строку для внутреннего представления объекта.
            grow: Базовый метод для увеличения высоты.
    """
    class ConiferousTree:
        def __init__(self, age: int, height: float) -> None:
            self.age = age
            self.height = height

        def __str__ (self) -> str:
            return f"A coniferous tree aged {self.age} years and {self.height} meters tall."

        def __repr__(self) -> str:
            return f"ConiferousTree(age={self.age}, height={self.height})"

        def grow(self) -> None:
            """
            Метод, который увеличивает высоту дерева.
            """
# TODO: описать дочерний класс
class Pine(ConiferousTree):
    """
        Дочерний класс Pine, наследующий ConiferousTree.
        Атрибуты:
            age (int): Возраст дерева.
            height (int): Высота дерева в метрах.
            type (str): Тип дерева.

        Методы:
            init: Расширяет конструктор базового класса.
            str: Перегружает строковое представление.
            grow: Перегружает метод для увеличения высоты.
        """
    def __init__(self, age: int, height: float, type: str) -> None:
        super().__init__(age, height, "pine")
        self.type = type

    def __str__(self) -> str:
        return f"{super().__str__()} is {self.type} pine."

    def grow(self, growth: float) -> None:
        self.height += growth




