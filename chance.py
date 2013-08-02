# -*- coding: utf-8 -*-
# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-08-02 20:37:54 (trhura)>

import random
import string
import linecache
import sys

def bool (likely=50):
    """
    Return a boolean value, either True or False. It has 50 percent chance
    of returning True, if not specified otherwise.

    :param likely: the likelihood of returning True

    >>> [bool (likely=100) for x in range(3)]
    [True, True, True]

    >>> [bool (likely=0) for x in range(3)]
    [False, False, False]
    """
    assert likely.__class__ in (int, float, long), "likely must be a number."
    assert 0 <= likely <= 100, "likely must be between 1 and 100."

    lstTrue = [True for x in range(likely)]
    lstFalse= [False for x in range(100-likely)]
    lst = lstTrue + lstFalse
    return random.choice (lst)

def character (pool=string.ascii_letters, skip=''):
    """
    Return a random character from pool. If not specified, `string.ascii_letters`
    will be used as pool. If *skip* is given, characters in *skip* will be ignored.

    :param  pool: a string or list of characters
    :param  skip: a string or list of blacklisted characters

    >>> character (pool='abcde', skip='abcd')
    'e'
    """
    assert pool.__class__ in [str,list], "Pool must be an iterable."
    assert skip.__class__ in [str,list], "Skip must be iterable."

    return random.choice ([p for p in pool if not p in skip])

def integer (min=-sys.maxint-1, max=sys.maxint):
    """
    Return a random integer between min and max (inclusive).

    :param min: integer to be used as minimum
    :param max: integer to be used as maximum
    >>> map (lambda x: 15 <= x <=20, [integer(min=15,max=17) for x in range(25)]) #doctest: +ELLIPSIS
    [True, ..., True, True]
    """
    assert min.__class__ == int, "Min must be a number"
    assert max.__class__ == int, "Max must be a number"
    assert min < max, "Minimum must be less than Maximum."

    return random.randint (min, max)

def number (around=100, plus_or_minus=25):
    """
    Return a random number around *around*, within *plus_or_minus* range.
    For example, `number (around=5, plus_or_minus=3)` will return a number x
    in range 2 <= x <= 8.

    :param around: integer to be used as base number
    :param plus_or_minus: integer
    >>> [number(around=25,plus_or_minus=10) for x in range(10)] #doctest: +SKIP
    [35, 27, 15, 17, 16, 25, 29, 31, 20, 30]

    """
    assert around.__class__ == int, "Min must be a number"
    assert plus_or_minus.__class__ == int, "Max must be a number"

    return random.randint (around-plus_or_minus, around+plus_or_minus)

def double (length=5):
    """
    Return a random float x between 0.0 <= x < 1.0. If length is specified,
    there will be `length` digits after decimal point.

    :param length: number of digits to follow after decimal point

    >>> [(16.8 + double (length=4) * 0.1, 96.1 + double (length=4)* 0.1)] #doctest: +SKIP
    [(16.8..., 96.1...)] # a random coordinate around Yangon (16.8, 96.1)
    """
    assert length.__class__ == int, "Length must be an integer"
    assert 0 < length < 10, "Should be 0 < length < 10"

    randfloat = random.random ()
    return float(str(randfloat)[:length + 2]) # FIXME:

def string (length=5, pool=string.ascii_letters, skip=''):
    """
    Return a random string of length containing characters from pool.
    If not specified, `string.ascii_letters` will be used as pool.
    If *skip* is given, characters in *skip* will be ignored.

    :param length: length of string
    :param  pool: a string or list of characters
    :param  skip: a string or list of blacklisted characters

    >>> string (length=6, pool='abcde', skip='abcd')
    'eeeeee'
    """
    return "".join (character(pool=pool,skip=skip) for x in range(length))

def word (regexp=""):
    """
    Return a random word matchin `regexp` expression from `/etc/dictionaries-common/words`.
    Currently it works only on Linux.

    :param regexp: ignored, currently not implemented yet
    """
    if not hasattr (word, 'lines'):
        with open ("/etc/dictionaries-common/words") as dictFile:
            word.lines = len (list(dictFile))

    return linecache.getline ("/etc/dictionaries-common/words",
                              random.randint (1, word.lines)).strip ()

def sentence (words=random.randint(5,12)):
    """
    Return a random sentence containing `n` words. Currently it
    works only on Linux.

    :param words: number of words in sentence
    """
    return " ".join ([word() for i in range(words)]).capitalize () + '.'

def paragraph (sentences=random.randint(5,12)):
    """
    Return a random paragraph containing `n` sentences. Currently it
    works only on Linux.

    :param sentences: number of sentences in paragraph
    """
    return " ".join ([sentence() for i in range(sentences)])

if __name__ == "__main__":
    import doctest
    doctest.testmod()