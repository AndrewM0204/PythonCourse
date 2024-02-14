class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        Book.__init__(self, name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError
        self._pages = pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        Book.__init__(self, name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, float):
            raise TypeError
        self._duration = duration


