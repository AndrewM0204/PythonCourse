class Parallelepiped:
    """
    Класс описывающий параллелепипед
    """
    def _init_(self, side1: float, side2: float, side3: float):
        """
        param side1, side2, side3: Стороны параллелепипеда
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def side_area(self) -> float:
        """
        return: Значение площади поверхности параллелепипеда
        """
        return 2*(self.side1*self.side2+self.side2*self.side3+self.side1*self.side3)

    def __str__(self):
        return f"{self.side1}x{self.side2}x{self.side3}"

    def __repr__(self):
        return f"{self.__class__.__name__}(side1={self.side1}, side2={self.side2}, side3={self.side3})"


class Cube(Parallelepiped):
    """
    Класс описывающий куб
    """
    def __init__(self, side: float):
        """
            param side: Сторона куба
        """
        self.side1 = self.side2 = self.side3 = side

    def side_area(self) -> float:
        """
        return: Значение площади поверхности куба

        Причина перегрузки: Использована более простая формула
        """
        return 6*self.side1**2

    def __repr__(self):
        """
        Причина перегрузки: Другой конструктор
        """
        return f"{self.__class__.__name__}(side={self.side1})"


if __name__ == "__main__":
    # Write your solution here
    pass
