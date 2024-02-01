# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class CoffeeMachine:
    def __init__(self, max_capasity: float, occupied_capasity: float):
        """
        param max_capasity: maximal capasity of machine
        param occupied_capasity: start capasity of machine

        >>> CoffeeMachine(100, 0).occupied_capasity
        0
        """
        if not isinstance(max_capasity, (int, float)):
            raise TypeError
        if max_capasity <= 0:
            raise ValueError
        if not isinstance(occupied_capasity, (int, float)):
            raise TypeError
        if occupied_capasity < 0:
            raise ValueError
        if occupied_capasity > max_capasity:
            raise ValueError
        self.max_capasity = max_capasity
        self.occupied_capasity = occupied_capasity

    def make_coffee(self, coffee_type: str) -> str:
        """
        Create record of coffee-making process

        param coffee_type: Type of coffee drink

        return: Record of coffee-making process
        """
        ...

    def refill(self, beans: float):
        """
        Increase occupied capasity of machine

        param beans: Number of coffee bean

        """
        if not isinstance(beans, (int, float)):
            raise TypeError
        if beans < 0:
            raise ValueError
        if beans+self.occupied_capasity > self.max_capasity:
            raise ValueError
        self.occupied_capasity += beans


class BookArchive:
    def __init__(self, books: list, is_editable: bool):
        """
        param books: List of books names in archive
        param is_editable: Flag of edit possibility

        >>> BookArchive([],False).is_editable
        False
        """
        self.books = books
        self.is_editable = is_editable

    def add_books(self, books: list):
        """
        Add books to the archive

        param books: List of books
        """
        if not self.is_editable:
            raise PermissionError
        ...

    def make_editable(self):
        """
        Make object edit possible
        """
        self.is_editable = True


class AffineOperator:
    def __init__(self, linear_part: list, translation_part: list):
        """
        param linear_part: 2x2 matrix
        param translation_part: 2 vector
        """
        if len(linear_part) != 4:
            raise ValueError
        if len(translation_part) != 2:
            raise ValueError
        self.linear_part = linear_part
        self.translation_part = translation_part

    def action(self, vector: list) -> list:
        """
        Action of operator on vector

        param vector: Argument of operator action

        return: Image of vector by operator

        >>> AffineOperator([1,0,0,1],[0,0]).action([1,0])
        [1, 0]
        """
        if len(vector) != 2:
            raise ValueError
        return vector

    def composition(self, right_multiplier: 'AffineOperator') -> 'AffineOperator':
        """
        param right_multiplier: AffineOperator object

        return: Composition of self as left multiplier and right_multiplier
        """
        if not isinstance(right_multiplier, AffineOperator):
            raise TypeError
        return self


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
