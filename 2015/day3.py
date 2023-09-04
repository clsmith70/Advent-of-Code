"""
    day3.py
    Advent of Code, 2015
    Day 3: Perfectly Spherical Houses in a Vacuum

    Santa is delivering presents to an infinite two-dimensional grid of houses.

    He begins by delivering a present to the house at his starting location, and 
    then an elf at the North Pole calls him via radio and tells him where to move 
    next. Moves are always exactly one house to the north (^), south (v), 
    east (>), or west (<). After each move, he delivers another present to the 
    house at his new location.

    Part 1: how many houses receive at least one present?
    Part 2: using robo-santa, how many houses receive at least one present?
"""
import sys
from pathlib import Path
import unittest

import numpy as np
from aoc15 import CityGrid

class GridTest(unittest.TestCase):
    """Test the grid"""
    def test_case1(self) -> None:
        """
            get one santa instruction, deliver to 2 houses
            get one santa and one robosanta instruction, deliver to 3 houses
        """
        grid = CityGrid(robo=False)
        robogrid = CityGrid(robo=True)
        grid.deliver('>')
        robogrid.deliver('^v')
        self.assertEqual(grid.count(), 2)
        self.assertEqual(robogrid.count(), 3)

    def test_case2(self) -> None:
        """
            get 4 santa instructions, deliver to 4 houses
            get 2 santa and 2 robosanta instructions, deliver to 3 houses
        """
        grid = CityGrid(robo=False)
        robogrid = CityGrid(robo=True)
        grid.deliver('^>v<')
        robogrid.deliver('^>v<')
        self.assertEqual(grid.count(), 4)
        self.assertEqual(robogrid.count(), 3)

    def test_case3(self) -> None:
        """
            get 10 santa instructions, deliver to 2 houses
            get 5 santa and 5 robosanta instructions, deliver to 11 houses
        """
        grid = CityGrid(robo=False)
        robogrid = CityGrid(robo=True)
        grid.deliver('^v^v^v^v^v')
        robogrid.deliver('^v^v^v^v^v')
        self.assertEqual(grid.count(), 2)
        self.assertEqual(robogrid.count(), 11)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    return Path(file_path).read_text(encoding='utf-8').strip()

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)
            santa_grid = CityGrid(robo=False)
            robo_grid = CityGrid(robo=True)
            santa_grid.deliver(data)
            robo_grid.deliver(data)

            print(f'Part 1: {santa_grid.count()}')
            print(f'Part 2: {robo_grid.count()}')
    else:
        # run tests
        unittest.main()
