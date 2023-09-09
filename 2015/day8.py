"""
    day8.py
    Advent of Code, 2015
    Day 8: Matchsticks

    Space on the sleigh is limited this year, and so Santa will be bringing his list
    as a digital copy. He needs to know how much space it will take up when stored.

    It is common in many programming languages to provide a way to escape special
    characters in strings. For example, C, JavaScript, Perl, Python, and even PHP
    handle special characters in very similar ways.

    However, it is important to realize the difference between the number of characters
    in the code representation of the string literal and the number of characters in
    the in-memory string itself.

    Santa's list is a file that contains many double-quoted string literals, one on
    each line. The only escape sequences used are \\ (which represents a single
    backslash), \" (which represents a lone double-quote character), and \ plus x and
    two hexadecimal characters (which represents a single character with that 
    ASCII code).

    Part 1: Disregarding the whitespace in the file, what is the number of characters
    of code for string literals minus the number of characters in memory for the values
    of the strings in total for the entire file?
    
    Part 2: Your task is to find the total number of characters to represent the newly
    encoded strings minus the number of characters of code in each original string
    literal.
"""
import sys
from pathlib import Path
import unittest

from aoc15 import SantasList

class SantasListTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """
            get the number of remaining characters when characters in memory is
            subtracted from characters in code, then get the difference between
            the number of encoded length and the original string length
        """
        test_data = [r'""', r'"abc"', r'"aaa\"aaa"', r'"\x27"']
        obj1 = SantasList(test_data)
        self.assertEqual(obj1.difference(), 12)
        self.assertEqual(obj1.encoded_difference(), 19)


def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            santas_list = SantasList(data)
            print(f'Part 1: {santas_list.difference()}')
            print(f'Part 2: {santas_list.encoded_difference()}')
    else:
        # run tests
        unittest.main()
