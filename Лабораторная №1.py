import doctest

class Apple:
    def __init__(self, color: str, weight: float):
        """
        Создание и подготовка к работе объекта "Яблоко"

        :param color: Цвет яблока
        :param weight: Вес яблока в граммах

        Примеры:
        >>> apple = Apple("red", 150)  # инициализация экземпляра класса
        """
        if not isinstance(color, str):
            raise TypeError("Цвет яблока должен быть строкой")
        self.color = color

        if not isinstance(weight, (int, float)):
            raise TypeError("Вес яблока должен быть типа int или float")
        if weight <= 0:
            raise ValueError("Вес яблока должен быть положительным числом")
        self.weight = weight

    def is_ripe(self) -> bool:
        """
        Функция, которая проверяет, спелое ли яблоко

        :return: Является ли яблоко спелым

        Примеры:
        >>> apple = Apple("red", 150)
        >>> apple.is_ripe()
        True
        >>> unripe_apple = Apple("green", 200)
        >>> unripe_apple.is_ripe()
        False
        """
        return self.color.lower() == "red"  # Предположим, что спелые яблоки всегда красные

    def eat(self, bites: int) -> str:
        """
        Метод для поедания яблока.

        :param bites: Количество откушенных кусочков

        :return: Сообщение о том, сколько кусочков было откушено

        Примеры:
        >>> apple = Apple("red", 150)
        >>> apple.eat(3)
        'Откушено 3 кусочка яблока.'
        """
        if not isinstance(bites, int) or bites <= 0:
            raise ValueError("Количество откушенных кусочков должно быть положительным целым числом")
        return f"Откушено {bites} кусочка яблока."


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
