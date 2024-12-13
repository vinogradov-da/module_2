import doctest


class Smartphone:
    def __init__(self, brand: str, model:str, memory: int):
        self.brand = brand
        self.model = model
        self.memory = memory
    def get_info(self) -> str:
        """
        Возвращает информацию о телефоне.
        >>> phone = Smartphone("Apple", "iPhone 12", 256)
        >>> phone.get_info()
        'Smartphone от Apple, iPhone 12, объем памяти 256 Gb'
        """
        return f'Smartphone от {self.brand}, {self.model}, объем памяти {self.memory} Gb'

    def set_memory(self, new_memory: int) -> None:
        """
        Устанавливает новый объем памяти.
        >>> phone = Smartphone("Apple", "iPhone 12", 256)
        >>> phone.set_memory(512)
        >>> phone.memory
        512
        """
        if new_memory < 0:
            raise ValueError("Объем памяти не может быть отрицательным")
        self.memory = new_memory


class Automobile:
    def __init__(self, model: str, color: str, speed: int):
        self.model = model
        self.color = color
        self.speed = speed

    def get_info(self) -> str:
        """
        Возвращает информацию о машине.
        >>> car = Automobile("Audi A6", "белый", 60)
        >>> car.get_info()
        'Audi A6, белый, зафиксированная скорость - 60 км/ч'
        """
        return f'{self.model}, {self.color}, зафиксированная скорость - {self.speed} км/ч'

    def change_speed (self, new_speed: int) -> None:
        """
        Изменяем значение скорости.
        >>> car = Automobile("Audi A6", "белый", 60)
        >>> car.change_speed(50)
        >>> car.speed
        50
        """
        if not isinstance(new_speed, (int, float)):
            raise TypeError("Изменяемая скорость должна быть типа int или float")
        if new_speed < 0:
            raise ValueError("Изменяемая скорость должна положительным числом")
        self.speed = new_speed


class Table:
    def __init__ (self, height: int, length: int):
        self.height = height
        self.length = length

    def get_info(self) -> str:
        """
        Возвращает информацию о столе.
        >>> folding_table = Table(70, 150)
        >>> folding_table.get_info()
        'Высота стола 70 см, длина - 150 см'
        """
        return f'Высота стола {self.height} см, длина - {self.length} см'

    def increase_length(self, new_length) -> None:
        """
        Изменяем длину стола.
        >>> folding_table = Table(70, 150)
        >>> folding_table.increase_length(200)
        >>> folding_table.length
        200
        """
        if not isinstance(new_length, (int, float)):
            raise TypeError("Значение длинны должна быть типа int или float")
        if new_length < 0:
            raise ValueError("Значение длинны должна быть положительным числом")
        self.length = new_length


if __name__ == "__main__":
    doctest.testmod()
