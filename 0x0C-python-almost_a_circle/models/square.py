#!/usr/bin/python3
"""A- Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ function"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ function"""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_square + str_id + str_xy + str_wh

    @property
    def size(self):
        """ size getter function"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter function"""
        self.width = value
        self.height = value

    def __str__(self):
        """__str__ function"""
        str_rectangle = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)

        return str_rectangle + str_id + str_xy + str_size

    def update(self, *args, **kwargs):
        """update function"""
        if args is not None and len(args) is not 0:
            list_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary function"""
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res
