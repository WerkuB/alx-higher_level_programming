#!/usr/bin/python3
'''task 6 module'''


class BaseGeometry:
    '''empty class'''
    def __init__(self):
        '''empty init'''
        pass

    def area(self):
        '''raise error for Area'''
        raise Exception('area() is not implemented')
