#!/usr/bin/python3
'''This module contains the definition of the Square Class'''


class Square:
    '''
    Defines a square
    
        size: the size of the square
    '''

    def __init__(self, size=0):
        '''Square Initialisation'''
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size