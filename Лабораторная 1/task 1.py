import doctest


class Human:
    """Класс описывающий человека"""
    def __init__(self, name: str, age: int, gender: str):
        """
        Инициализация человека
        :param name: Имя человека
        :param age: Возраст человека
        :param gender: Пол человека
        """
        if age < 0:
            raise ValueError('Возраст не может быть меньше 0')
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self) -> str:
        """
        Вывести краткое описание человека
        :return: Строка с описанием человека
        """
        return f'Привет, меня зовут {self.name}, мне {self.age} лет, я {self.gender}.'

    def __repr__(self):
        """
        Строковое представление объекта
        :return: Строка с информацией об объекте
        """
        return f'Human(name={self.name}, age={self.age}, gender={self.gender})'


class Car:
    """Класс описывающий машину"""
    def __init__(self, model: str, color: str, speed: int):
        """
        Инициализация машины
        :param model: Модель машины
        :param color: Цвет машины
        :param speed: Максимальная скорость
        """
        if speed < 0:
            raise ValueError('Скорость не может быть меньше 0')
        self.model = model
        self.color = color
        self.speed = speed

    def accelerate(self, delta: int) -> int:
        """
        Увеличить скорость машины на заданную величину
        :param delta: Величина, на которую нужно увеличить скорость
        :return: Текущая скорость машины
        """
        self.speed += delta
        return self.speed

    def brake(self) -> int:
        """
        Остановить машину
        :return: Текущая скорость машины
        """
        self.speed = 0
        return self.speed

    def __repr__(self):
        """
        Строковое представление объекта
        :return: Строка с информацией об объекте
        """
        return f'Car(model={self.model}, color={self.color}, speed={self.speed})'


class Airplane:
    """Класс описывающий самолёт"""
    def __init__(self, model: str, capacity: int, altitude: int):
        """
        Инициализация самолёта
        :param model: Модель самолёта
        :param capacity: Вместимость самолёта
        :param altitude: Текущая высота полёта
        """
        if altitude < 0:
            raise ValueError('Высота не может быть меньше 0')
        self.model = model
        self.capacity = capacity
        self.altitude = altitude

    def ascend(self, delta: int) -> int:
        """
        Подняться на заданную высоту
        :param delta: Величина, на которую нужно подняться
        :return: Текущая высота полёта
        """
        self.altitude += delta
        return self.altitude

    def descend(self) -> int:
        """
        Опуститься на землю
        :return: Текущая высота полёта
        """
        self.altitude = 0
        return self.altitude

    def __repr__(self):
        """
        Строковое представление объекта
        :return: Строка с информацией об объекте
        """
        return f'Airplane(model={self.model}, capacity={self.capacity}, altitude={self.altitude})'

    if __name__ == '__main__':
        doctest.testmod()
