from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @property
    def area(self):
        return self.get_area()

    @property
    def perimeter(self):
        return self.get_perimeter()

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(
                "Передан объект, не являющийся геометрической фигурой"
            )
        return self.get_area() + figure.get_area()
