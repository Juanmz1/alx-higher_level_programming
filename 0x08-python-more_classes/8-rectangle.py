#!/usr/bin/python3
""" Define a class rectangle """


class Rectangle:
    """ class of rectangle """
    number_of_instances = 0
    print_symbol = "#"

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ a static method that returns the biggest rectangle based on the area """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """ initialize the rectangle """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    def __del__(self):
        """ print a string when a instances have been deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
    @property
    def width(self):
        """ getter of the private instances attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter of the private instancez attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter of the private instances attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of the private instancez attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__height = value
    def area(self):
        """ that returns the rectangle area """
        return self.__width * self.__height
    def perimeter(self):
        """ that returns the rectangle perimeter """
        if self.__width != 0 and self.__height != 0:
            return ((self.__width + self.__height) * 2)
        return 0
    def __str__(self):
        """ print the rectangle with the character # """
        strg = ""
        if self.__width != 0 and self.__height != 0:
            strg += "\n".join(str(self.print_symbol) * self.__width
                                for j in range(self.__height))
        return strg
    def __repr__(self):
        """ return a string representation of the rectangle        to be able to recreate a new instances
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
