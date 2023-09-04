"""
    day6.py
    Advent of Code, 2015
    Day 6: Probably a Fire Hazard

    Because your neighbors keep defeating you in the holiday house decorating 
    contest year after year, you've decided to deploy one million lights in a 
    1000x1000 grid.

    Furthermore, because you've been especially nice this year, Santa has 
    mailed you instructions on how to display the ideal lighting configuration.

    Lights in your grid are numbered from 0 to 999 in each direction; the 
    lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The 
    instructions include whether to turn on, turn off, or toggle various 
    inclusive ranges given as coordinate pairs. Each coordinate pair represents 
    opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 
    through 2,2 therefore refers to 9 lights in a 3x3 square. 
    
    The lights all start turned off.

    To defeat your neighbors this year, all you have to do is set up your 
    lights by doing the instructions Santa sent you in order.

    Part 1: how many lights are lit following the directions?

    You just finish implementing your winning light pattern when you realize 
    you mistranslated Santa's message from Ancient Nordic Elvish.

    The light grid you bought actually has individual brightness controls; 
    each light can have a brightness of zero or more. The lights all start 
    at zero.

    The phrase turn on actually means that you should increase the brightness 
    of those lights by 1.

    The phrase turn off actually means that you should decrease the brightness 
    of those lights by 1, to a minimum of zero.

    The phrase toggle actually means that you should increase the brightness 
    of those lights by 2.

    Part 2: what is the total brightness of all lights combined after following
        Santa's instructions?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import LightGrid

class LightGridTest(unittest.TestCase):
    """Test the grid object"""
    def test_case1(self) -> None:
        """Test part 1 example"""
        test_grid = LightGrid()
        test_grid.set_on([0,0], [999,999])
        test_grid.toggle([0,0], [999,0])
        test_grid.set_off([499,499], [500,500])
        self.assertEqual(test_grid.count(), 998_996)

    def test_case2(self) -> None:
        """Test part 2 example"""
        test_grid2 = LightGrid()
        test_grid2.set_on([0,0], [0,0], version=2)
        test_grid2.toggle([0,0], [999,999], version=2)
        self.assertEqual(test_grid2.count(), 2_000_001)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

def parse_line(inst_data: str) -> list[str, list[int, int], list[int, int]]:
    """parse the instruction for processing"""
    inst_data = inst_data.split()

    if inst_data[0] == 'toggle':
        instruction = inst_data[0]
        start_x, start_y = inst_data[1].split(',')
        end_x, end_y = inst_data[3].split(',')
        start = [int(start_x), int(start_y)]
        end = [int(end_x), int(end_y)]
    else:
        instruction = inst_data[1]
        start_x, start_y = inst_data[2].split(',')
        end_x, end_y = inst_data[4].split(',')
        start = [int(start_x), int(start_y)]
        end = [int(end_x), int(end_y)]

    return instruction, start, end

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)
            lightshow = LightGrid()
            lightshow2 = LightGrid()

            for line in data:
                inst, starting, ending = parse_line(line)
                if inst == 'toggle':
                    lightshow.toggle(starting, ending)
                    lightshow2.toggle(starting, ending, version=2)
                elif inst == 'on':
                    lightshow.set_on(starting, ending)
                    lightshow2.set_on(starting, ending, version=2)
                elif inst == 'off':
                    lightshow.set_off(starting, ending)
                    lightshow2.set_off(starting, ending, version=2)

            print(f'Part 1: {lightshow.count()}')
            print(f'Part 2: {lightshow2.count()}')
    else:
        # run tests
        unittest.main()
