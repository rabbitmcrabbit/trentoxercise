#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Debugging example adapted from a nice tutorial by Jeremy Jones,
http://onlamp.com/pub/a/python/2005/09/01/debugger.html?page=1
"""

import string
import sys
import unittest

class ConvertToDict:
    """Split a line of text into integer values and store them in a dictionary.

    For example, the line
    "1234 2345 3456 4567"

    is converted to
    {'1': 2345, '0': 1234, '3': 4567, '2': 3456}
    """

    def __init__(self):
        self.tmp_dict = {}

    def walk_string(self, some_string):
        """Walk given text string and return a dictionary. 
        Maintain state in instance attributes in case we hit an exception"""
        self.reset()
        l = string.split(some_string)
        for i in range(len(l)):
            key = str(i)
            self.tmp_dict[key] = int(l[i])
        return_dict = self.tmp_dict
        return return_dict

    def reset(self):
        """Clean up"""
        self.tmp_dict = {}

    def get_number_dict(self, some_string):
        """Do super duper exception handling here"""
        try:
            return self.walk_string(some_string)
        except:
            # if we hit an exception, we can rely on tmp_dict 
            # being a backup to the point of the exception
            return self.tmp_dict
            
class FirstTestCase(unittest.TestCase):
    def testStateConfusion(self):
        cases = [
            ('1234 2345 3456 4567', {'0': 1234, '1': 2345, '2': 3456, '3': 4567}),
            ('9876 8765 7654 6543', {'0': 9876, '1': 8765, '2': 7654, '3': 6543}),
            ]
        ctd = ConvertToDict()

        for query, result in cases:
            self.assertEqual(ctd.get_number_dict(query), result)
            
        ctd.get_number_dict('13 34 34 34 34 34 34 14\x0815 16 17')
        
        for query, result in cases:
            self.assertEqual(ctd.get_number_dict(query), result)
        

def main():
    ctd = ConvertToDict()
    # read a file line by line, convert it to a dictionary,
    # and print the results
    for line in file(sys.argv[1]):
        line = line.strip()
        print "*" * 40
        print "line>>", line
        print ctd.get_number_dict(line)
        print "*" * 40
    
if __name__ == "__main__":
    #main()
    unittest.main()
