"""
    day4.py
    Advent of Code, 2015
    Day 4: The Ideal Stocking Stuffer

    Santa needs help mining some AdventCoins (very similar to bitcoins) to use 
    as gifts for all the economically forward-thinking little girls and boys.

    To do this, he needs to find MD5 hashes which, in hexadecimal, start with 
    at least five zeroes. The input to the MD5 hash is some secret key (your 
    puzzle input, given below) followed by a number in decimal. To mine 
    AdventCoins, you must find Santa the lowest positive number (no leading 
    zeroes: 1, 2, 3, ...) that produces such a hash.

    Part 1: which value is first to have a hash starting with 00000 (5 zeros)?
    Part 2: which value is first to have a hash starting with 000000 (6 zeros)?

    My Input: iwrupvqb
"""
import sys
import unittest

from hashlib import md5

class AdventCoin(object):
    """An (almost) infinte delivery grid"""
    CHECK_RANGE = 1_000_000_000
    def __init__(self, key: str, match: str) -> None:
        self.key = key
        self.match = match

    def md5hash(self) -> int:
        """what func does"""
        for i in range(self.CHECK_RANGE):
            hash_value = md5(f"{self.key}{i}".encode())
            if hash_value.hexdigest()[:len(self.match)] == self.match:
                return i
        return None

class AdventCoinTest(unittest.TestCase):
    """Test the advent coin"""
    def test_case1(self) -> None:
        """
            test with abcdef, which should produce 609043
        """
        coin1 = AdventCoin('abcdef', '00000')
        value1 = coin1.md5hash()
        self.assertEqual(value1, 609043)

    def test_case2(self) -> None:
        """
            test with pqrstuv, which should return 1048970
        """
        coin2 = AdventCoin('pqrstuv', '00000')
        value2 = coin2.md5hash()
        self.assertEqual(value2, 1048970)

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for value in sys.argv[1:]:
            print(f"\nkey = {value}:")
            advent_coin1 = AdventCoin(value, '00000')
            advent_coin2 = AdventCoin(value, '000000')

            print(f'Part 1: {advent_coin1.md5hash()}')
            print(f'Part 2: {advent_coin2.md5hash()}')
    else:
        # run tests
        unittest.main()
