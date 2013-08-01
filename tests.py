# -*- coding: utf-8 -*-
# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-08-01 21:59:56 (trhura)>

import unittest
import string
from chance import Chance

class ChanceTest (unittest.TestCase):
    def setUp (self):
        pass

    def test_bool_raises_exceptions (self):
        self.assertRaises (AssertionError, Chance.bool, likely='nonsese')
        self.assertRaises (AssertionError, Chance.bool, likely=101)

    def test_bool_return_true_and_false (self):
        bools = [Chance.bool () for i in range(25)]
        self.assertIn (True, bools,
                       "There should be a True.")
        self.assertIn (False, bools,
                       "There should be a False.")

    def test_bool_likely_argument (self):
        bools = [Chance.bool (likely=0) for i in range (25)]
        self.assertNotIn (True, bools,
                          "There should not a True.")

        bools = [Chance.bool (likely=100) for i in range(25)]
        self.assertNotIn (False, bools,
                          "There should not be a False")

    def test_character_is_in_pool (self):
        chars = [Chance.character (pool=string.digits) for x in range(50)]
        map (lambda c: self.assertIn (c, string.digits), chars)

if __name__ == "__main__":
    unittest.main ()
