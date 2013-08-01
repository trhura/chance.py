# -*- coding: utf-8 -*-
# Author: Thura Hlaing <trhura@gmail.com>
# Time-stamp: <2013-08-01 23:27:26 (trhura)>

import unittest
import string
import chance

class ChanceTest (unittest.TestCase):
    def setUp (self):
        pass

    def test_bool_raises_exceptions (self):
        self.assertRaises (AssertionError, chance.bool, likely='nonsese')
        self.assertRaises (AssertionError, chance.bool, likely=101)

    def test_bool_return_true_and_false (self):
        bools = [chance.bool () for i in range(25)]
        self.assertIn (True, bools,
                       "There should be a True.")
        self.assertIn (False, bools,
                       "There should be a False.")

    def test_bool_likely_argument (self):
        bools = [chance.bool (likely=0) for i in range (25)]
        self.assertNotIn (True, bools,
                          "There should not a True.")

        bools = [chance.bool (likely=100) for i in range(25)]
        self.assertNotIn (False, bools,
                          "There should not be a False")

    def test_character_is_in_pool (self):
        chars = [chance.character (pool=string.digits) for x in range(25)]
        map (lambda c: self.assertIn (c, string.digits), chars)

if __name__ == "__main__":
    unittest.main ()
