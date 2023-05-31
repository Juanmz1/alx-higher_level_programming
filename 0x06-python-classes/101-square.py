#!/usr/bin/python3
""" define class square """


class Square:
    """ Represent a square
    Attributes:
    __size(int): size of the square
    """
    def __init__(self, size = 0, position = (0, 0)):
        """ initialize a square
        Args:
        __size(int): size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of a size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError(size must be an integer)
        elif size < 0:
            raise ValueError(size must be >= 0)
        else:
            self.__size = value

    @property
    def position(self):
        """ Get the current position of the size
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the setter fot the current position
        """
        msg = "position must be in a tuple of 2 positive integers"
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise TypeError(msg)
            else:
                raise TypeError(msg)
        else:
            raise TypeError(msg)

    def area(self):
        """ Define area of square
        Returns: Area of square
        """
        return self.__size ** 2

    def my_print(self):
        """ prints the square
        Returns: None
        """
        if self.__size == 0:
            print()
            return
        if self.__size != 0:
            print("\n" * self.position[1], end='')
        for i in range(self.__size):
            print(" " * self.__position[0], end='')
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
    def __str__(self):
        """prints to stdout the square with #

        Returns:
            final string
        """

        res = ""
        if self.__size != 0:
            res = "\n" * self.position[1]
        for i in range(self.__size):
            res += " " * self.__position[0]
            for j in range(self.__size):
                res += "#"
            if i != (self.__size - 1):
                result += "\n"
        return res
