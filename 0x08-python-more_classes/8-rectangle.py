#!/usr/bin/python3
'''class that defines new Rectangle '''


class Rectangle:
    '''new Class'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Object desctructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        ''' a property to retrieve the value of width '''
        return(self.__width)

    @width.setter
    def width(self, value):
        ''' property setter to set the value of width '''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):

        return self.__height

    @height.setter
    def height(self, value):
        ''' propoerty setter to set the value of hight '''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        ''' Public method to compute the area'''

        return self.__height * self.__width

    def perimeter(self):
        '''public method to compute the perimeter'''

        if self.__height == 0 or self.__width == 0:
            return 0

        else:
            return self.__height * 2 + self.__width * 2

    def __str__(self):
        ''' print readable form of object '''

        s = ""

        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                s += str(self.print_symbol)
            s += '\n'
        s = s[:-1]

        return s

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Static method to compare two Rectangle of class Rectangle'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return(rect_1)
        else:
            return(rect_2)

    def __repr__(self):
        ''' print the object representation '''

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
