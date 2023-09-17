"""
    day18.py
    Advent of Code, 2015
    Day 18: Like a GIF For Your Yard

    Description from site

    Part 1: ???
    Part 2: ???
"""
import sys
from pathlib import Path
import unittest

from aoc15 import AnimatedLights

class AnimatedLightsTest(unittest.TestCase):
    """Test the object"""

    TEST_GRID1 = [
        '.#.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####..'
    ]

    TEST_GRID2 = [
        '##.#.#',
        '...##.',
        '#....#',
        '..#...',
        '#.#..#',
        '####.#'
    ]

    def test_case1(self) -> None:
        """test with all lights working properly"""
        obj1 = AnimatedLights(self.TEST_GRID1, steps=4)
        self.assertEqual(obj1.count(), 4)

    def test_case2(self) -> None:
        """test with corner lights stuck on"""
        obj2 = AnimatedLights(self.TEST_GRID2, conway=True, steps=5)
        self.assertEqual(obj2.count(), 17)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    path = Path(file_path)

    with open(path, 'r') as file:
        data = [line.strip() for line in file.readlines()]

    return data

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            lights_p1 = AnimatedLights(data)
            print(f'Part 1: {lights_p1.count()}')
            lights_p2 = AnimatedLights(data, conway=True)
            print(f'Part 2: {lights_p2.count()}')
    else:
        # run tests
        unittest.main()
