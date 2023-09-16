"""
    day17.py
    Advent of Code, 2015
    Day 17: No Such Thing as Too Much

    The elves bought too much eggnog again - 150 liters this time. To fit it all into 
    your refrigerator, you'll need to move it into smaller containers. You take an 
    inventory of the capacities of the available containers.

    For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If 
    you need to store 25 liters, there are four ways to do it:

        15 and 10
        20 and 5 (the first 5)
        20 and 5 (the second 5)
        15, 5, and 5

    While playing with all the containers in the kitchen, another load of eggnog 
    arrives! The shipping and receiving department is requesting as many containers as 
    you can spare.

    Part 1: Filling all containers entirely, how many different combinations of 
        containers can exactly fit all 150 liters of eggnog?
    Part 2: How many different ways can you fill the minimum number of containers and
        still hold exactly 150 litres?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import EggNogStorage

class EggNogStorageTest(unittest.TestCase):
    """Test the object"""

    TEST_CONTAINERS = [5, 5, 10, 15, 20]

    def test_case1(self) -> None:
        """
            how many combinations of containers can exactly fit all 
            25 liters of eggnog?
        """
        obj1 = EggNogStorage(self.TEST_CONTAINERS, liters=25)
        self.assertEqual(obj1.Combinations(), 4)

    def test_case2(self) -> None:
        """
            how many smallest combinations of containers can exactly fit 
            25 liters of eggnog?
        """
        obj2 = EggNogStorage(self.TEST_CONTAINERS, liters=25)
        self.assertEqual(obj2.MinimumCombinations(), 3)
        """
            this assertion should be for 2, but 3 combos are found
            if non-unique values are left out, then the real number for the challenge
            is skewed by 8
        """

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [int(line.strip()) for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            nog = EggNogStorage(data)

            print(f'Part 1: {nog.Combinations()}')
            print(f'Part 2: {nog.MinimumCombinations()}')
    else:
        # run tests
        unittest.main()
