"""
    day15.py
    Advent of Code, 2015
    Day 15: Science for Hungry People

    Today, you set out on the task of perfecting your milk-dunking cookie recipe. All 
    you have to do is find the right balance of ingredients.

    Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list 
    of the remaining ingredients you could use to finish the recipe (your puzzle input) 
    and their properties per teaspoon:

        capacity (how well it helps the cookie absorb milk)
        durability (how well it keeps the cookie intact when full of milk)
        flavor (how tasty it makes the cookie)
        texture (how it improves the feel of the cookie)
        calories (how many calories it adds to the cookie)

    You can only measure ingredients in whole-teaspoon amounts accurately, and you have 
    to be accurate so you can reproduce your results in the future. The total score of 
    a cookie can be found by adding up each of the properties (negative totals become 
    0) and then multiplying together everything except calories.

    Part 1: ???
    Part 2: ???
"""
import sys
from pathlib import Path
import unittest

from aoc15 import Cookie

class CookieTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """
            what is the optimal score using 100 tsp of the test ingredients
        """
        test_ingredients1 = ['Butterscotch: capacity -1, durability -2, flavor 6, \
                texture 3, calories 8','Cinnamon: capacity 2, durability 3, flavor -2, \
                texture -1, calories 3']
        obj = Cookie(test_ingredients1)
        self.assertEqual(obj.score(), 62842880)
        self.assertEqual(obj.score_500cal(), 57600000)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            cookie = Cookie(data)
            print(f'Part 1: {cookie.score()}')
            print(f'Part 2: {cookie.score_500cal()}')
    else:
        # run tests
        unittest.main()
