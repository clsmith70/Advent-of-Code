"""
    day13.py
    Advent of Code, 2015
    Day 13: Knights of the Dinner Table

    In years past, the holiday feast with your family hasn't gone so well. Not everyone 
    gets along! This year, you resolve, will be different. You're going to find the 
    optimal seating arrangement and avoid all those awkward conversations.

    You start by writing up a list of everyone invited and the amount their happiness 
    would increase or decrease if they were to find themselves sitting next to each 
    other person. You have a circular table that will be just big enough to fit 
    everyone comfortably, and so each person will have exactly two neighbors.

    Part 1: ???
    Part 2: ???
"""
import sys
from pathlib import Path
import unittest

from aoc15 import Happiness

class HappinessTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """
            Import the test case data from the day13.test file, then find the optimal
            seating arrangement (highest happiness score)
        """
        test_data1 = read_data('data/day13.test')
        obj = Happiness(test_data1)
        obj.calculate_happiness()
        self.assertEqual(obj.happiness(), 330)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            party = Happiness(data)
            party.calculate_happiness()
            print(f'Part 1: {party.happiness()}')

            party.add_host()
            party.calculate_happiness()
            print(f'Part 2: {party.happiness()}')
    else:
        # run tests
        unittest.main()
