#!/usr/bin/python3
""" student module to define student class """


class Student:
    """ define student class """
    def __init__(self, first_name, last_name, age):
        """ init modules """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ dictionary representation """
        d = self.__dict__
        if attrs is None:
            return ({k: v for (k, v) in reversed(d.items())})
        elif all(isinstance(x, str) for x in attrs):
            return ({k: v for (k, v) in reversed(d.items()) if k in attrs})
        else:
            return ({k: v for (k, v) in reversed(d.items())})
