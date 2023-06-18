#!/usr/bin/python3
""" 'square.py' module """
from models.rectangle import Rectangle



class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    
    def __init__(self, size, x=0, y=0, id=None):
        """ initialization of the Square model """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter of the size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter of the size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the class Square by adding the public method """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ print out the dixtionary representation of the square """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    def __str__(self):
        """ string representation of the square """
        return "[Sqaure] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

