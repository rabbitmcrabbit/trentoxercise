# Advanced Scientific Programming in Python, autumn school, Trento, 2010
# Day 1, Exercise 1 (unit testing and coverage)
# Author: Pietro Berkes <berkes _at_ brandeis _dot_ edu>

import unittest

def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """

    if type(x) != type([]):
        message = 'Input argument must be a list, got %s instead' % type(x)
        raise TypeError(message)

    idx = []

    # if it is too short, there are no local maxima
    if len(x)<2:
        return []

    # left hand case
    if x[0] > x[1]:
        idx.append(0)

    # middle bits
    for i in range(1,len(x)-1):
        # `i` is a local maximum if the signal decreases before and after it
        if x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)

    # right hand case
    if x[-1]>x[-2]:
        idx.append(len(x)-1)

    # return
    return idx

    # NOTE for the curious: the code above could be written using
    # list comprehension as
    # return [i for i in range(len(x)) if x[i-1]<x[i] and x[i+1]<x[i]]
    # not that this would solve the bugs ;-)



class MyTestCase(unittest.TestCase):

    # where the maxima lie on the border
    def test_borders(self):
        testcases = [
            ([1,2],[1]),
            ([2,1],[0]),
            ([5],[]),
            ([1,2,3],[2]),
            ([3,2,1],[0]),
            ([3,1,2],[0,2]),
            ([4,1,2,3],[0,3])]
        for (arg,result) in testcases:
            self.assertEqual(find_maxima(arg),result)

    # examples from the exercise sheet
    def test_exercise(self):
        testcases = [
            ([0,1,2,1,2,1,0],[2,4]),
            ([i**2 for i in range(-3,4)], [0, 6]),
            ([4,2,1,3,1,2], [0,3,5]),
            ([4,2,1,3,1,5], [0,3,5]),
            ([4,2,1,3,1], [0, 3])]
        for (arg,result) in testcases:
            self.assertEqual(find_maxima(arg),result)

    # argument is correctly types
    def test_dog(self):
        self.assertRaises(TypeError,find_maxima,'dog')


if __name__=='__main__':
    unittest.main()
