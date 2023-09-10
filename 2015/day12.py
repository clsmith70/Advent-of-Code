"""
    day12.py
    Advent of Code, 2015
    Day 12: JSAbacusFramework.io

    Santa's Accounting-Elves need help balancing the books after a recent order. 
    Unfortunately, their accounting software uses a peculiar storage format. That's 
    where you come in.

    They have a JSON document which contains a variety of things: arrays ([1,2,3]), 
    objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find 
    all of the numbers throughout the document and add them together.

    For example:

        [1,2,3] and {"a":2,"b":4} both have a sum of 6.
        [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
        {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
        [] and {} both have a sum of 0.

    You will not encounter any strings containing numbers.

    Part 1: What is the sum of all numbers in the document?
    Part 2: Uh oh - the Accounting-Elves have realized that they double-counted 
        everything red.

        Ignore any object (and all of its children) which has any property with the 
        value "red". Do this only for objects ({...}), not arrays ([...]).
"""
import sys
import json
import unittest

from aoc15 import JSAbacus

class JSAbacusTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """Add up all the numbers"""
        test_data1 = [1,2,3]
        obj1 = JSAbacus(test_data1)
        self.assertEqual(obj1.sum(), 6)

    def test_case2(self) -> None:
        """Add up all the numbers"""
        test_data2 = {"a":{"b":4},"c":-1}
        obj2 = JSAbacus(test_data2)
        self.assertEqual(obj2.sum(), 3)

    def test_case3(self) -> None:
        """Add up all the numbers"""
        test_data3 = [-1,{"a":1}]
        obj3 = JSAbacus(test_data3)
        self.assertEqual(obj3.sum(), 0)

    def test_case4(self) -> None:
        """Add up all the numbers"""
        test_data4 = []
        obj4 = JSAbacus(test_data4)
        self.assertEqual(obj4.sum(), 0)

    def test_case5(self) -> None:
        """Add up all the numbers, with a filter"""
        test_data5 = [1,{"c":"red","b":2},3]
        obj5 = JSAbacus(test_data5, 'red')
        self.assertEqual(obj5.sum(), 4)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    with open(file_path, "r") as abacus_data:
        json_data = json.load(abacus_data)
    return json_data

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            abacus = JSAbacus(data)
            print(f'Part 1: {abacus.sum()}')

            abacus.set_filter('red')
            abacus.reprocess()
            print(f'Part 2: {abacus.sum()}')
    else:
        # run tests
        unittest.main()
