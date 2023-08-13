"""
    day1.py
    Advent of Code, 2015
    Day 1: Not Quite Lisp

    Santa is trying to deliver presents in a large apartment building, but he 
    can't find the right floor - the directions he got are a little confusing. 
    He starts on the ground floor (floor 0) and then follows the instructions 
    one character at a time.

    An opening parenthesis, (, means he should go up one floor, and a closing 
    parenthesis, ), means he should go down one floor.

    The apartment building is very tall, and the basement is very deep; he 
    will never find the top or bottom floors.

    Part 1: What floor do the instructions take Santa to?
    Part 2: Which instruction causes Santa to first enter the basement?
"""
import sys
from pathlib import Path
import unittest

class Elevator(object):
    """The elevator to go between floors"""
    # the instruction number that first enters the basement
    _first_negative = 0
    _negative_occurred = False
    _instruction_count = 0

    def __init__(self) -> None:
        self.floor = 0

    def move(self, instructions: str) -> None:
        """change floors according to the instructions"""
        for direction in instructions:
            if direction == '(': # go up
                self.floor += 1
                self._instruction_count += 1
            elif direction == ')': # go down
                self.floor -= 1
                self._instruction_count += 1
                if self.floor < 0 and self._negative_occurred is False:
                    self._first_negative = self._instruction_count
                    self._negative_occurred = True

    def get_basement_entry(self):
        """Get the instruction number of first basement entry"""
        return f"Instruction {self._first_negative}"

    def __repr__(self):
        return f"Floor {self.floor}"

class TestElevator(unittest.TestCase):
    """Test the class"""
    def test_case1(self):
        """Test a result returning to floor 0"""
        test_elevator = Elevator()
        test_elevator.move('(())')
        self.assertEqual(str(test_elevator), "Floor 0")
        self.assertEqual(test_elevator.get_basement_entry(), "Instruction 0")

    def test_case2(self):
        """Test a result ending on floor 3"""
        test_elevator = Elevator()
        test_elevator.move('(()(()(')
        self.assertEqual(str(test_elevator), "Floor 3")
        self.assertEqual(test_elevator.get_basement_entry(), "Instruction 0")

    def test_case3(self):
        """Test a result ending on floor -3"""
        test_elevator = Elevator()
        test_elevator.move(')())())')
        self.assertEqual(str(test_elevator), "Floor -3")
        self.assertEqual(test_elevator.get_basement_entry(), "Instruction 1")

def read_data(file_path: str) -> str:
    """read processing data from the file specified"""
    return Path(file_path).read_text(encoding='utf-8').strip()

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)
            elevator = Elevator()
            elevator.move(data)
            print(f'Part 1: {elevator}')
            print(f'Part 2: {elevator.get_basement_entry()}')
    else:
        # run tests
        unittest.main()
