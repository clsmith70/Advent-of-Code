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

class CityGrid(object):
    """An (almost) infinte delivery grid"""

    def __init__(self, robo: bool = False) -> None:
        self._delivery_count: int = 0
        self._grid = np.zeros((10_000, 10_000), dtype=int)
        """
            index 0 is north/south and index 1 is east/west
            start santa and robosanta in the middle of the grid
        """
        self._santa: tuple = [4_999, 4_999]
        self._robosanta: tuple = [4_999, 4_999]
        self._roboturn: bool = False
        self._delivery_count = 1
        if robo:
            self._grid[self._santa[0], self._santa[1]] += 2
        else:
            self._grid[self._santa[0], self._santa[1]] += 1
        self.robo = robo

    def deliver(self, directions: str) -> None:
        """deliver gifts within the grid"""
        for direction in directions:
            if self.robo:
                if self._roboturn:
                    self._robosanta = self._move(direction, self._robosanta)
                    self._visit_position(self._robosanta)
                    self._roboturn = not self._roboturn
                else:
                    self._santa = self._move(direction, self._santa)
                    self._visit_position(self._santa)
                    self._roboturn = not self._roboturn
            else:
                self._santa = self._move(direction, self._santa)
                self._visit_position(self._santa)

    def _move(self, direction: str,
             position: tuple[int, int]) -> tuple[int, int]:
        """move one grid square in the indicated direction"""
        if direction == '^': # move north
            position[0] += 1
        elif direction == 'v': # move south
            position[0] -= 1
        elif direction == '<': # move west
            position[1] -= 1
        elif direction == '>': # move east
            position[1] += 1
        return position
    
    def _visit_position(self, position: tuple[int, int]) -> None:
        """check to see if this grid position was previously visited"""
        if self._grid[position[0], position[1]] == 0:
            self._delivery_count += 1

        # add a visit to the position
        self._grid[position[0], position[1]] += 1

    def count(self) -> int:
        """return the count of houses that received at least one gift"""
        return self._delivery_count

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
