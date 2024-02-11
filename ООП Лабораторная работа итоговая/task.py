if __name__ == "__main__":
    class Entity:
        """
        Базовый класс для сущностей.
        """

        def __init__(self, name: str):
            """
            Конструктор класса Entity.

            :param name: Название сущности.
            """
            self.name = name

        def __str__(self) -> str:
            return f"Сущность: {self.name}"

        def __repr__(self) -> str:
            return f"Сущность(name={self.name})"


    class Car(Entity):
        """
        Дочерний класс для автомобилей.
        """

        def __init__(self, name: str, brand: str):
            """
            Конструктор класса Car.

            :param name: Название автомобиля.
            :param brand: Марка автомобиля.
            """
            super().__init__(name)
            self.brand = brand

        def drive(self, distance: int) -> str:
            """
            Метод для езды на автомобиле.

            :param distance: Расстояние, которое нужно проехать.
            :return: Сообщение о пройденном расстоянии.
            """
            return f"{self.brand} {self.name} проехала {distance} км."

        def __str__(self) -> str:
            return f"Машина: {self.brand} {self.name}"

        def __repr__(self) -> str:
            return f"Машина(name={self.name}, марка={self.brand})"
