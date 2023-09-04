"""
    day5.py
    Advent of Code, 2015
    Day 5: Doesn't He Have Intern-Elves For This?

    Santa needs help figuring out which strings in his text file are naughty or nice.

    A nice string is one with all of the following properties:

        - It contains at least three vowels (aeiou only), like aei, xazegov, or 
        aeiouaeiouaeiou.
        - It contains at least one letter that appears twice in a row, like xx, 
        abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
        - It does not contain the strings ab, cd, pq, or xy, even if they are 
        part of one of the other requirements.

    Part 1: how many strings are nice?

    Realizing the error of his ways, Santa has switched to a better model of 
    determining whether a string is naughty or nice. None of the old rules 
    apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:

        - It contains a pair of any two letters that appears at least twice in 
        the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but 
        not like aaa (aa, but it overlaps).
        - It contains at least one letter which repeats with exactly one letter 
        between them, like xyx, abcdefeghi (efe), or even aaa.
 
    Part 2: how many strings are nice under the new rules?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import NiceString

class NiceTest(unittest.TestCase):
    """Test the object"""
    def test_original_rules(self) -> None:
        """
            test case description
        """
        original1 = NiceString('ugknbfddgicrmopn')
        original2 = NiceString('aaa')
        original3 = NiceString('jchzalrnumimnmhp')
        original4 = NiceString('haegwjzuvuyypxyu')
        original5 = NiceString('dvszwmarrgswjxmb')
        self.assertEqual(original1.check_rules(), True)
        self.assertEqual(original2.check_rules(), True)
        self.assertEqual(original3.check_rules(), False)
        self.assertEqual(original4.check_rules(), False)
        self.assertEqual(original5.check_rules(), False)

    def test_new_rules(self) -> None:
        """
            test case description
        """
        new1 = NiceString('qjhvhtzxzqqjkmpb')
        new2 = NiceString('xxyxx')
        new3 = NiceString('uurcxstgmygtbstg')
        new4 = NiceString('ieodomkazucvgmuy')
        self.assertEqual(new1.check_new_rules(), True)
        self.assertEqual(new2.check_new_rules(), True)
        self.assertEqual(new3.check_new_rules(), False)
        self.assertEqual(new4.check_new_rules(), False)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)
            nice_v1: int = 0
            nice_v2: int = 0

            for line in data:
                santa_string = NiceString(line)
                if santa_string.check_rules():
                    nice_v1 += 1

                if santa_string.check_new_rules():
                    nice_v2 += 1
                    
            print(f'Part 1: {nice_v1}')
            print(f'Part 2: {nice_v2}')
    else:
        # run tests
        unittest.main()
