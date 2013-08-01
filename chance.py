# -*- coding: utf-8 -*-
# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-08-01 22:01:03 (trhura)>

import random
import string

class Chance (object):
    """
    Chance Object
    """
    def __init__ (self):
        pass

    @classmethod
    def bool (cls, likely=50):
        """
        Return a boolean value, either True or False. It has 50 percent chance
        of returning True, if not specified otherwise.

        :param likely: the likelihood of returning True

        >>> [Chance.bool (likely=100) for x in range(3)]
        [True, True, True]

        >>> [Chance.bool (likely=0) for x in range(3)]
        [False, False, False]
        """
        assert likely.__class__ in (int, float, long)
        assert 0 <= likely <= 100

        lstTrue = [True for x in range(likely)]
        lstFalse= [False for x in range(100-likely)]
        lst = lstTrue + lstFalse
        return random.choice (lst)

    @classmethod
    def character (cls, pool=string.ascii_letters, skip=''):
        """
        Return a random character from pool. If not specified, `string.ascii_letters`
        will be used as pool. If `skip` is given, characters in `skip` will be ignored.

        :param  pool: a string or list of characters
        :param  skip: a string or list of blacklisted characters

        >>> Chance.character (pool='abcde', skip='abcd')
        'e'
        """
        return random.choice ([p for p in pool if not p in skip])

if __name__ == "__main__":
    import doctest
    doctest.testmod()