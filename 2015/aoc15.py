import numpy as np
from hashlib import md5
import re

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

class Present(object):
    """A present to be wrapped"""

    def __init__(self, length: int, width: int, height: int) -> None:
        self.length = length
        self.width = width
        self.height = height

    def sorted_dimensions(self) -> tuple[int, int, int]:
        """return the sorted side sizes"""
        dimensions = self.length, self.width, self.height
        return sorted(dimensions)

    def get_total_paper(self) -> int:
        """calculate the total square feet of paper need to wrap this present"""
        dimensions = self.sorted_dimensions()
        smallest_side = dimensions[0] * dimensions[1]

        return ((2 * self.length * self.width) +
                (2 * self.width * self.height) +
                (2 * self.height * self.length) + smallest_side)

    def get_total_ribbon(self) -> int:
        """calculate the feet of ribbon required for the perfect bow"""
        dimensions = self.sorted_dimensions()
        ribbon_length = (dimensions[0] * 2) + (dimensions[1] * 2)
        bow_length = self.length * self.width * self.height

        return ribbon_length + bow_length

class CityGrid(object):
    """An (almost) infinte delivery grid"""

    def __init__(self, robo: bool = False) -> None:
        self._delivery_count: int = 0
        self._grid = np.zeros((10_000, 10_000), dtype=int)
        """
            index 0 is north/south and index 1 is east/west
            start santa and robosanta in the middle of the grid
        """
        self._santa: tuple = [4_999, 4_999]
        self._robosanta: tuple = [4_999, 4_999]
        self._roboturn: bool = False
        self._delivery_count = 1
        if robo:
            self._grid[self._santa[0], self._santa[1]] += 2
        else:
            self._grid[self._santa[0], self._santa[1]] += 1
        self.robo = robo

    def deliver(self, directions: str) -> None:
        """deliver gifts within the grid"""
        for direction in directions:
            if self.robo:
                if self._roboturn:
                    self._robosanta = self._move(direction, self._robosanta)
                    self._visit_position(self._robosanta)
                    self._roboturn = not self._roboturn
                else:
                    self._santa = self._move(direction, self._santa)
                    self._visit_position(self._santa)
                    self._roboturn = not self._roboturn
            else:
                self._santa = self._move(direction, self._santa)
                self._visit_position(self._santa)

    def _move(self, direction: str,
             position: tuple[int, int]) -> tuple[int, int]:
        """move one grid square in the indicated direction"""
        if direction == '^': # move north
            position[0] += 1
        elif direction == 'v': # move south
            position[0] -= 1
        elif direction == '<': # move west
            position[1] -= 1
        elif direction == '>': # move east
            position[1] += 1
        return position
    
    def _visit_position(self, position: tuple[int, int]) -> None:
        """check to see if this grid position was previously visited"""
        if self._grid[position[0], position[1]] == 0:
            self._delivery_count += 1

        # add a visit to the position
        self._grid[position[0], position[1]] += 1

    def count(self) -> int:
        """return the count of houses that received at least one gift"""
        return self._delivery_count

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

class NiceString(object):
    """A class to check if a string is nice under North Pole rules"""

    REGEX_A = re.compile(r"(.)\1")
    REGEX_B = re.compile(r"ab|cd|pq|xy")
    MATCHSET = 'aeiou'

    def __init__(self, string: str) -> None:
        self._is_nice = False
        self.string = string

    def _get_char_count(self) -> int:
        work_string = self.string.casefold()
        count = {}.fromkeys(self.MATCHSET, 0)
        for character in work_string:
            if character in count:
                count[character] += 1
        return sum(count.values())

    def check_rules(self) -> bool:
        """check if the string is nice under the original rules"""
        if self._get_char_count() >= 3:
            if self.REGEX_A.findall(self.string):
                if not self.REGEX_B.findall(self.string):
                    return True
        return False

    def check_new_rules(self) -> None:
        """check if the string is nice under the new rules"""
        if not any([self.string[i] == self.string[i+2] 
                    for i in range(len(self.string)-2)]):
            return False
        if any([self.string.count(self.string[i: i+2]) >= 2
                for i in range(len(self.string) -2)]):
            return True
        return False

class LightGrid(object):
    """An object to represent the problem"""

    def __init__(self, grid_x:int=1_000, grid_y:int=1_000) -> None:
        self.lights = np.zeros((grid_x, grid_y), dtype=int)
        self._count = 0

    def toggle(self, start:list[int, int],
               end:list[int, int], version:int=1) -> None:
        """Toggle the lights"""
        if version == 1:
            # turn on/off
            for x_pos in range(start[0], end[0] + 1):
                for y_pos in range(start[1], end[1] + 1):
                    self.lights[x_pos, y_pos] = not self.lights[x_pos, y_pos]
        else:
            # increase brightness by 2
            for x_pos in range(start[0], end[0] + 1):
                for y_pos in range(start[1], end[1] + 1):
                    self.lights[x_pos, y_pos] += 2

    def set_on(self, start:list[int, int],
               end:list[int, int], version:int=1) -> None:
        """turn lights on"""
        if version == 1:
            # turn or leave lights on
            for x_pos in range(start[0], end[0] + 1):
                for y_pos in range(start[1], end[1] + 1):
                    self.lights[x_pos, y_pos] = 1
        else:
            # increase the brightness
            for x_pos in range(start[0], end[0] + 1):
                for y_pos in range(start[1], end[1] + 1):
                    self.lights[x_pos, y_pos] += 1

    def set_off(self, start:list[int, int],
               end:list[int, int], version:int=1) -> None:
        """turn lights off"""
        if version == 1:
            # turn or leave lights off
            for x_pos in range(start[0], end[0] + 1):
                for y_pos in range(start[1], end[1] + 1):
                    self.lights[x_pos, y_pos] = 0
        else:
            # decrease the brightness
            for x_pos in range(start[0], end[0] + 1):
                for y_pos in range(start[1], end[1] + 1):
                    if self.lights[x_pos, y_pos] > 1:
                        self.lights[x_pos, y_pos] -= 1
                    else:
                        self.lights[x_pos, y_pos] = 0

    def count(self) -> int:
        """return the object's count"""
        return np.sum(self.lights)

class Circuit(object):
    """
        An object to represent the circuit
        _gates are the list of gates and their outputs
        change_signal indicates if the signal on a gate should be altered
        prior to executing the instruction set.  If change_signal is set
        to True, change_gate and change_value must be supplied.
    """

    def __init__(self, instructions:list, change_signal:bool=False,
                change_gate:str=None, change_value:int=None) -> None:
        self._gates = {}
        self._load_gates([i.split(' -> ') for i in instructions])
        if change_signal:
            self._gates[change_gate] = int(change_value)
        self._execute()
        for gate in self._gates:
            print(f"{gate} = {self._gates[gate]}")

    def _load_gates(self, instructions:list) -> None:
        """Load the initial instructions into the gates"""
        for inst in instructions:
            self._gates[inst[1]] = inst[0]

    def _check_value(self, gate:str) -> bool:
        """Check if gate contains an int value"""
        if isinstance(self._gates[gate], int):
            return True
        return False

    def _is_finished(self) -> bool:
        """Check all gates for int, any str returns False"""
        is_finished = True
        for key in self._gates:
            if not isinstance(self._gates[key], int):
                is_finished = False
        return is_finished

    def _execute(self) -> None:
        """Run the loaded instructions until there are no """
        while not self._is_finished():
            for key in self._gates:
                if self._check_value(key):
                    continue

                temp = self._gates[key].split()
                if len(temp) == 1:
                    if isinstance(temp, list):
                        self._gates[key] = int(temp[0])
                    else:
                        self._gates[key] = int(temp)
                elif len(temp) == 2: # NOT
                    if self._check_value(temp[1]):
                        value = ~int(self._gates[temp[1]])
                        if value < 0:
                            self._gates[key] = value + 65536
                        else:
                            self._gates[key] = value
                elif len(temp) == 3: # LSHIFT, RSHIFT, AND, OR
                    """
                        check each temp value to see if it is an int
                        if it is, cast and use.  if it is not, get that
                        value from self._gates, then check that value - repeat
                    """
                    if self._check_value(temp[0]):
                        tgate = int(self._gates[temp[0]])
                        if temp[1] == 'LSHIFT':
                            self._gates[key] = tgate << int(temp[2])
                        elif temp[1] == 'RSHIFT':
                            self._gates[key] = tgate >> int(temp[2])
                        elif temp[1] == 'AND':
                            if self._check_value(temp[2]):
                                tgate2 = int(self._gates[temp[2]])
                                self._gates[key] = tgate & tgate2
                        elif temp[1] == 'OR':
                            if self._check_value(temp[2]):
                                tgate2 = int(self._gates[temp[2]])
                                self._gates[key] = tgate | tgate2

    def get(self, gate:str) -> int:
        """return the value of the requested gate"""
        return self._gates[gate]

class SantasList(object):
    """An object to represent the problem"""

    def __init__(self, data:list) -> None:
        self._code_length = 0
        self._memory_length = 0
        self._encoded_memory_length = 0
        self._list = data
        self._process_code()

    def _process_code(self) -> None:
        """loop over the list and total up the code and memory lengths"""
        for line in self._list:
            self._code_length += len(line)
            self._memory_length += len(eval(line))
            self._encoded_memory_length += line.count('\\') + line.count('"') + 2

    def difference(self) -> int:
        """return the difference between code and memory lengths"""
        return self._code_length - self._memory_length
    
    def encoded_difference(self) -> int:
        """return the difference between the encoded strings and the original strings"""
        return self._encoded_memory_length

