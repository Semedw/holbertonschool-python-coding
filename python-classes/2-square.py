#!/usr/bin/python3
"""
This script create an object and it checks whether the size is suitible or not
"""


class Square:
    """
    This class create a square object
    """
    def __init__(self, size=0):
        """
        This method run when an object is initialized
        """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
    
    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size**2
