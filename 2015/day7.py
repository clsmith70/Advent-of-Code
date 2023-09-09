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

class Circuit(object):
    """
        An object to represent the circuit
        _gates are the list of gates and their outputs
        change_signal indicates if the signal on a gate should be altered
        prior to executing the instruction set.  If change_signal is set
        to True, change_gate and change_value must be supplied.
    """

    def __init__(self, instructions:list, gate_of_interest:str,
                 change_signal:bool=False, change_gate:str=None,
                 change_value:int=None) -> None:
        self._gates = {}
        self._gate_of_interest = gate_of_interest
        self._load_gates([i.split(' -> ') for i in instructions])
        if change_signal:
            self._gates[change_gate] = int(change_value)
        self._execute()
        # for gate, value in self._gates.items():
        #     print(f"{gate} = {value}")

    def _load_gates(self, instructions:list) -> None:
        """Load the initial instructions into the gates"""
        for inst in instructions:
            self._gates[inst[1]] = inst[0]

    def _check_value(self, value:str, gate:bool=True) -> bool:
        """Check if gate contains an int value"""
        if gate:
            try:
                if isinstance(int(self._gates[value]), int):
                    return True
            except (KeyError, ValueError):
                return False
        else:
            try:
                if isinstance(int(value), int):
                    return True
            except (ValueError, TypeError):
                return False

    def _is_finished(self) -> bool:
        """Check all gates for int, any str returns False"""
        try:
            if not isinstance(int(self._gates[self._gate_of_interest]), int):
                return False
        except ValueError:
            return False
        return True

    def _get_result(self, value1:int, value2:int, operand:str) -> int:
        """Peform the requested operation and return the result"""
        retval = 0

        if operand == 'LSHIFT':
            retval = value1 << value2
        elif operand == 'RSHIFT':
            retval = value1 >> value2
        elif operand == 'AND':
            retval = value1 & value2
        elif operand == 'OR':
            retval = value1 | value2
        elif operand == 'NOT':
            retval = ~int(value1)
            if retval > 65535:
                retval = retval - 65536
            elif retval < 0:
                retval = retval + 65536
        

        return retval

    def _execute(self) -> None:
        """Run the loaded instructions until there are no """
        while not self._is_finished():
            for key, value in self._gates.items():
                if self._check_value(value, False):
                    continue

                temp = value.split()
                if len(temp) == 1 and self._check_value(temp, False):
                    self._gates[key] = int(temp)

                elif len(temp) == 1 and isinstance(temp, list):
                    if self._check_value(temp[0], True):
                        self._gates[key] = int(self._gates[temp[0]])
                
                elif len(temp) == 2 and self._check_value(temp[1], True):
                    self._gates[key] = self._get_result(int(self._gates[temp[1]]),
                                            None, temp[0])

                elif len(temp) == 2 and self._check_value(temp[1], False):
                    self._gates[key] = self._get_result(int(temp[1]), None, temp[0])

                elif (len(temp) == 3 and self._check_value(temp[0], True)
                      and self._check_value(temp[2], True)):
                    v1, v2 = int(self._gates[temp[0]]), int(self._gates[temp[2]])
                    self._gates[key] = self._get_result(v1, v2, temp[1])
                
                elif (len(temp) == 3 and self._check_value(temp[0], False)
                      and self._check_value(temp[2], True)):
                    v1, v2 = int(temp[0]), int(self._gates[temp[2]])
                    self._gates[key] = self._get_result(v1, v2, temp[1])
                
                elif (len(temp) == 3 and self._check_value(temp[0], True)
                      and self._check_value(temp[2], False)):
                    v1, v2 = int(self._gates[temp[0]]), int(temp[2])
                    self._gates[key] = self._get_result(v1, v2, temp[1])
                
                elif (len(temp) == 3 and self._check_value(temp[0], False)
                      and self._check_value(temp[2], False)):
                    v1, v2 = int(temp[0]), int(temp[2])
                    self._gates[key] = self._get_result(v1, v2, temp[1])

    def get(self, gate:str) -> int:
        """return the value of the requested gate"""
        return self._gates[gate]

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
