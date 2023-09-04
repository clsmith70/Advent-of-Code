"""
    day2.py
    Advent of Code, 2015
    Day 2: I Was Told There Would Be No Math

    The elves are running low on wrapping paper, and so they need to submit an 
    order for more. They have a list of the dimensions (length l, width w, and 
    height h) of each present, and only want to order exactly as much as 
    they need.

    Fortunately, every present is a box (a perfect right rectangular prism), 
    which makes calculating the required wrapping paper for each gift a little
    easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. 
    The elves also need a little extra paper for each present: the area of the 
    smallest side.  All numbers in the elves list are in feet.

    The elves are also running low on ribbon. Ribbon is all the same width, 
    so they only have to worry about the length they need to order, which they 
    would again like to be exact.

    The ribbon required to wrap a present is the shortest distance around its 
    sides, or the smallest perimeter of any one face. Each present also 
    requires a bow made out of ribbon as well; the feet of ribbon required for 
    the perfect bow is equal to the cubic feet of volume of the present. Don't 
    ask how they tie the bow, though; they'll never tell.

    Part 1: How many square feet of wrapping paper should they order?
    Part 2: How many feet of ribbon should they order?
"""
import sys
from pathlib import Path
import unittest

import re
from aoc15 import Present

class TestPresent(unittest.TestCase):
    """Test the present"""
    def test_case1(self) -> None:
        """Test a present of dimensions 2x3x4"""
        test_present = Present(2, 3, 4)
        self.assertEqual(test_present.get_total_paper(), 58)
        self.assertEqual(test_present.get_total_ribbon(), 34)

    def test_case2(self):
        """Test a present of dimensions 1x1x10"""
        test_present = Present(1, 1, 10)
        self.assertEqual(test_present.get_total_paper(), 43)
        self.assertEqual(test_present.get_total_ribbon(), 14)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line for line in raw_data.split('\n')]

def get_dimensions(raw_dimensions: str) -> tuple[int, int, int]:
    """split a present line on 'x' and return a 3 int tuple"""
    side_a, side_b, side_c = re.split('x', raw_dimensions)
    return int(side_a), int(side_b), int(side_c)

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)
            total_paper: int = 0
            total_ribbon: int = 0

            for line in data:
                l, w, h = get_dimensions(line)
                present = Present(l, w, h)
                total_paper += present.get_total_paper()
                total_ribbon += present.get_total_ribbon()

            print(f'Part 1: {total_paper}')
            print(f'Part 2: {total_ribbon}')
    else:
        # run tests
        unittest.main()
