#!/usr/bin/python3
'''
This module contains the definition of the Square Class
'''


class Square:
    '''
    Defines a square

        size: the size of the square
    '''

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
    
my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)