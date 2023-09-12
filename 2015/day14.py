"""
    day14.py
    Advent of Code, 2015
    Day 14: TITLE

    This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest 
    occasionally to recover their energy. Santa would like to know which of his 
    reindeer is fastest, and so he has them race.

    Reindeer can only either be flying (always at their top speed) or resting (not 
    moving at all), and always spend whole seconds in either state.

    Part 1: What distance did the winning reindeer travel?
    Part 2: How many points does the winning reindeer have?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import Reindeer

class ReindeerTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """which reindeer flys the furthest after 1000 seconds of racing?"""
        data = ['Comet can fly 14 km/s for 10 seconds, but then must rest for \
                127 seconds.', 'Dancer can fly 16 km/s for 11 seconds, but then must \
                    rest for 162 seconds.']
        obj = Reindeer(data, 'distance', 1000)
        self.assertEqual(obj.winner(), "Comet, 1120")

    def test_case2(self) -> None:
        """which reindeer earns the most points after 1000 seconds of racing"""
        data = ['Comet can fly 14 km/s for 10 seconds, but then must rest for \
                127 seconds.', 'Dancer can fly 16 km/s for 11 seconds, but then must \
                    rest for 162 seconds.']
        obj2 = Reindeer(data, 'points', 1000)
        self.assertEqual(obj2.winner(), "Dancer, 689")

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            race1 = Reindeer(data)
            print(f'Part 1: {race1.winner()}')

            race2 = Reindeer(data, 'points')
            print(f'Part 2: {race2.winner()}')
    else:
        # run tests
        unittest.main()
