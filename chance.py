# -*- coding: utf-8 -*-
# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-08-01 21:06:21 (trhura)>

import random

class Chance (object):

    def __init__ (self):
        pass


    @classmethod
    def bool (cls, likely=50):
        """
        ..      py:staticmethod:: bool ([likely=50])
                Return a boolean value, either True or False

                :param likely: the likelihood of returning True
                :type  likely: Integer
        """
        assert likely.__class__ in (int, float, long)
        assert 0 <= likely <= 100

        likely  = likely if likely else 50
        lstTrue = [True for x in range(likely)]
        lstFalse= [False for x in range(100-likely)]
        lst = lstTrue + lstFalse
        return random.choice (lst)


if __name__ == "__main__":
    pass