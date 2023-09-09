"""
    day9.py
    Advent of Code, 2015
    Day 9: All in a Single Night

    Every year, Santa manages to deliver all of his presents in a single night.

    This year, however, he has some new locations to visit; his elves have provided him
    the distances between every pair of locations. He can start and end at any two 
    (different) locations he wants, but he must visit each location exactly once. What 
    is the shortest distance he can travel to achieve this?

    Part 1: What is the distance of the shortest route?
    Part 2: What is the distance of the longest route?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import Travel

class TravelTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """
            What is the distance of the shortest route?
        """
        test_distances = ['London to Dublin = 464', 'London to Belfast = 518', 
                       'Dublin to Belfast = 141']
        obj = Travel(test_distances)
        self.assertEqual(obj.shortest(), 605)
        self.assertEqual(obj.longest(), 982)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            santas_trip = Travel(data)
            print(f'Part 1: {santas_trip.shortest()}')
            print(f'Part 2: {santas_trip.longest()}')
    else:
        # run tests
        unittest.main()
