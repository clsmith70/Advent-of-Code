"""
    day11.py
    Advent of Code, 2015
    Day 11: Corporate Policy

    Santa's previous password expired, and he needs help choosing a new one.

    To help him remember his new password after the old one expires, Santa has devised 
    a method of coming up with a password based on the previous one. Corporate policy 
    dictates that passwords must be exactly eight lowercase letters (for security 
    reasons), so he finds his new password by incrementing his old password string 
    repeatedly until it is valid.

    Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. 
    Increase the rightmost letter one step; if it was z, it wraps around to a, and 
    repeat with the next letter to the left until one doesn't wrap around.

    Unfortunately for Santa, a new Security-Elf recently started, and he has imposed 
    some additional password requirements:

    Passwords must include one increasing straight of at least three letters, like abc, 
        bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
    Passwords may not contain the letters i, o, or l, as these letters can be mistaken 
        for other characters and are therefore confusing.
    Passwords must contain at least two different, non-overlapping pairs of letters, 
        like aa, bb, or zz.

    Part 1: Given Santa's current password, what shoudl his next password be?
    Part 2: Santa's password has expired again.  What's the next one?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import PasswordPolicy

class PasswordPolicyTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """
            check test passwords and get next passwords as required
        """
        obj1 = PasswordPolicy('jijklmmn')
        self.assertEqual(obj1.is_valid(), False)

    def test_case2(self) -> None:
        obj2 = PasswordPolicy('abbceffg')
        self.assertEqual(obj2.is_valid(), False)
    
    def test_case3(self) -> None:
        obj3 = PasswordPolicy('abbcegjk')
        self.assertEqual(obj3.is_valid(), False)

    def test_case4(self) -> None:
        obj4 = PasswordPolicy('abcdefgh')

        while not obj4.is_valid():
            obj4.next_password()
        self.assertEqual(obj4.get_password(), 'abcdffaa')

    def test_case5(self) -> None:
        obj5 = PasswordPolicy('ghijklmn')

        while not obj5.is_valid():
            obj5.next_password()
        self.assertEqual(obj5.get_password(), 'ghjaabcc')

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    return Path(file_path).read_text(encoding='utf-8').strip()

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)

            password_policy = PasswordPolicy(data)
            while not password_policy.is_valid():
                password_policy.next_password()
            print(f'Part 1: {password_policy.get_password()}')

            password_policy.next_password()
            while not password_policy.is_valid():
                password_policy.next_password()
            print(f'Part 2: {password_policy.get_password()}')
    else:
        # run tests
        unittest.main()
