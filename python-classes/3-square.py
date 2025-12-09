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

    def area(self):
        """
        Calculates the area of the square
        """
        return self.__size**2
    
    @property
    def size(self):
        """
        Property for the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter of the size of square
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

