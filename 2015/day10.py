"""
    day10.py
    Advent of Code, 2015
    Day 10: Elves Look, Elves Say

    Today, the Elves are playing a game called look-and-say. They take turns making 
    sequences by reading aloud the previous sequence and using that reading as the next 
    sequence. For example, 211 is read as "one two, two ones", which becomes 1221 
    (1 2, 2 1s).

    Look-and-say sequences are generated iteratively, using the previous value as input 
    for the next step. For each step, take the previous value, and replace each run of 
    digits (like 111) with the number of digits (3) followed by the digit itself (1).

    Part 1: Starting with the digits in your puzzle input, apply this process 40 
    times. What is the length of the result?

    Part 2: Now, starting again with the digits in your puzzle input, apply this 
    process 50 times. What is the length of the new result?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import ElfSay

class ElfSayTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """
            Run a simple test staring with '1' and repeating 4 times
        """
        obj = ElfSay('1', 4)
        self.assertEqual(obj.count(), 6)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    return Path(file_path).read_text(encoding='utf-8').strip()

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            elf_say1 = ElfSay(data, 40)
            print(f'Part 1: {elf_say1.count()}')

            elf_say2 = ElfSay(data, 50)
            print(f'Part 2: {elf_say2.count()}')
    else:
        # run tests
        unittest.main()
