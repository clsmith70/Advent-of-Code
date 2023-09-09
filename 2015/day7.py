"""
    day7.py
    Advent of Code, 2015
    Day 7: Some Assembly Required

    This year, Santa brought little Bobby Tables a set of wires and bitwise 
    logic gates! Unfortunately, little Bobby is a little under the recommended 
    age range, and he needs help assembling the circuit.

    Each wire has an identifier (some lowercase letters) and can carry a 16-bit 
    signal (a number from 0 to 65535). A signal is provided to each wire by a 
    gate, another wire, or some specific value. Each wire can only get a signal 
    from one source, but can provide its signal to multiple destinations. A 
    gate provides no signal until all of its inputs have a signal.

    The included instructions booklet describes how to connect the parts 
    together: x AND y -> z means to connect wires x and y to an AND gate, 
    and then connect its output to wire z.

    Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, 
    for some reason, you'd like to emulate the circuit instead, almost all 
    programming languages (for example, C, JavaScript, or Python) provide 
    operators for these gates.

    Part 1: What is the value of gate 'a' after executing?
    Part 2: What is the value of gate 'a' after setting 'b' to the value of'a'
        from Part 1 and executing?
"""
import sys
from pathlib import Path
import unittest

from aoc15 import Circuit

class CircuitTest(unittest.TestCase):
    """Test the object"""
    def test_case1(self) -> None:
        """Test a small circuit, the result should be 72"""
        test_data = ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e',
            'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h','NOT y -> i',
            '1 AND x -> j']
        test_circuit1 = Circuit(test_data, 'd')
        self.assertEqual(test_circuit1.get('d'), 72)

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)
            
            part1 = Circuit(data, 'a')
            print(f'Part 1: {part1.get("a")}')

            part2 = Circuit(data, 'a', True, 'b', part1.get('a'))
            print(f'Part 2: {part2.get("a")}')
    else:
        # run tests
        unittest.main()
