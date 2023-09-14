from math import prod
import numpy as np
from hashlib import md5
import re
import random
from itertools import permutations

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

class Travel(object):
    """An object to represent the problem"""

    def __init__(self, distances:list) -> None:
        self._shortest = 9_999_999
        self._longest = 0
        self._distances = distances
        self._table = {}
        self._load_table()
        self._calculate_paths()

    def _load_table(self) -> None:
        """load the distance data"""
        for route in self._distances:
            path = route.split()
            source = path[0]
            destination = path[2]
            distance = int(path[-1])

            if source in self._table.keys():
                self._table[source].append((destination, distance))
            else:
                self._table[source] = [(destination, distance)]

            if destination in self._table.keys():
                self._table[destination].append((source, distance))
            else:
                self._table[destination] = [(source, distance)]
            
    def _path_cost(self, path:str) -> int:
        """calculate the cost of a path"""
        total = 0
        path = list(path)

        while len(path) > 1:
            current_path = path.pop(0)
            destinations = self._table[current_path]

            for (distance, cost) in destinations:
                if distance == path[0]:
                    total += cost
                    break

        return total
    
    def _calculate_paths(self) -> None:
        """calculate the paths to find the shortest and longest"""
        for path in permutations(self._table.keys()):
            trip = self._path_cost(path)
            if trip < self._shortest:
                self._shortest = trip
            if trip > self._longest:
                self._longest = trip

    def shortest(self) -> int:
        """return the shortest path cost"""
        return self._shortest
    
    def longest(self) -> int:
        """return the longest path cost"""
        return self._longest

class ElfSay(object):
    """An object to represent the problem"""

    def __init__(self, starter:str, repeat:int) -> None:
        self._data = starter
        for _ in range(repeat):
            self._look()

    def _look(self) -> None:
        """use the current self._data to loop through a look-and-say loop"""
        result = ""
        value = self._data
        while not value == "":
            (said, value) = self._say(value)
            result += said
        self._data = result
    
    def _say(self, value:str) -> None:
        """say the first value in the string with the count of how many there are"""
        x = value[0]
        count = 0

        for char in value:
            if char == x:
                count += 1
            else:
                break

        remaining = value[count:]
        return(str(count) + x, remaining)

    def _func2(self) -> None:
        """what func2 does"""

    def count(self) -> int:
        """return the object's count"""
        return len(self._data)

class PasswordPolicy(object):
    """An object to represent the problem"""
    CHARS = 'abcdefghjkmnpqrstuvwxyz'
    DOUBLES = [char + char for char in CHARS]
    RUNS = [''.join(r) for r in zip(CHARS[:-2], CHARS[1:-1], CHARS[2:])]
    NEXT_CHAR = {char1: char2 for char1, char2 in zip(CHARS, CHARS[1:] + 'a')}

    def __init__(self, initial_password:str=None) -> None:
        self._password = initial_password

    def set_password(self, password:str) -> None:
        """load a password to test or get the next one for"""
        self._password = password

    def next_password(self) -> str:
        """get the next password according to the rules"""
        test = r"ilo"
        if any(elem in self._password for elem in test):
            self._password = self._password.replace('i', 'j')
            self._password = self._password.replace('l', 'm')
            self._password = self._password.replace('o', 'p')

        password = self._password[:-1] + self.NEXT_CHAR[self._password[-1]]

        for i in range(-1, -8, -1):
            if password[i] == 'a':
                password = password[:i -1] + \
                    self.NEXT_CHAR[password[i - 1]] + password[i:]
            else:
                break
        
        self._password = password

    def is_valid(self) -> bool:
        """check the validity of the currently loaded password"""
        test = r"ilo"
        if any(elem in self._password for elem in test):
            return False

        if sum([pair in self._password for pair in self.DOUBLES]) < 2:
            return False
        
        if not any([run in self._password for run in self.RUNS]):
            return False
        
        return True
    
    def get_password(self) -> str:
        """return the stored password"""
        return self._password

class JSAbacus(object):
    """An object to represent the problem"""

    def __init__(self, jsData:str, filter:str=None) -> None:
        self._sum = 0
        self._jsdata = jsData
        self._filter = filter
        self._process_dict(self._jsdata)

    def set_filter(self, filter:str) -> None:
        """set or change the filter"""
        self._filter = filter

    def reprocess(self) -> None:
        """start the process over"""
        self._sum = 0
        self._process_dict(self._jsdata)

    def _process_dict(self, data:str) -> None:
        """process a json dict"""
        if isinstance(data, dict):
            if self._filter is not None:
                if self._filter not in data.values():
                    for _, value in data.items():
                        if isinstance(value, dict):
                            self._process_dict(value)
                        elif isinstance(value, list):
                            self._process_list(value)
                        elif isinstance(value, int):
                            self._sum += value
            else:
                for _, value in data.items():
                    if isinstance(value, dict):
                        self._process_dict(value)
                    elif isinstance(value, list):
                        self._process_list(value)
                    elif isinstance(value, int):
                        self._sum += value
        else:
            self._process_list(data)

    def _process_list(self, data:str) -> None:
        """process a json list"""
        if isinstance(data, list):
            for key in data:
                if isinstance(key, dict):
                    self._process_dict(key)
                elif isinstance(key, list):
                    self._process_list(key)
                elif isinstance(key, int):
                    self._sum += key
        else:
            self._process_dict(data)

    def sum(self) -> int:
        """return the object's count"""
        return self._sum

class Happiness(object):
    """An object to represent the problem"""

    def __init__(self, seating:list) -> None:
        self._happiness = []
        self._guest_list = {}
        self._create_guest_list(seating)

    def add_host(self) -> None:
        """add the host to the guest list and reset the score list"""
        for key, _ in self._guest_list.items():
            self._guest_list[key].append(('Host', 0))

        self._guest_list['Host'] = []
        for key, _ in self._guest_list.items():
            self._guest_list['Host'].append((key, 0))

        self._happiness = []

    def _create_guest_list(self, data) -> None:
        """set up the guest list with happiness scores"""
        for line in data:
            guest1, _, state, score, _, _, _, _, _, _, guest2 = line.split()
            # remove the . after guest2's name
            guest2 = guest2[:-1]
            # convert the score to an int
            if state == 'lose':
                score = -int(score)
            else:
                score = int(score)

            if guest1 in self._guest_list:
                self._guest_list[guest1].append((guest2, score))
            else:
                self._guest_list[guest1] = [(guest2, score)]

    def _get_neighbor(self, group:list, person:str) -> tuple:
        """returns the neighor on each side of the person indicated"""
        position = group.index(person)

        if position == 0:
            return (group[position + 1], group[-1])
        elif position == len(group) - 1:
            return (group[position -1], group[0])
        else:
            return (group[position - 1], group[position + 1])
    
    def _get_score(self, person:str, nextTo:str) -> int:
        """get the score for the seating arrangement"""
        values = self._guest_list[person]

        for (neighbor, score) in values:
            if neighbor == nextTo:
                return score
            
    def _get_happiness(self, group:tuple) -> int:
        """get the happiness score of the current permutation"""
        happiness = 0

        for g in group:
            (a, b) = self._get_neighbor(list(group), g)
            happiness += self._get_score(g, a)
            happiness += self._get_score(g, b)

        return happiness

    def calculate_happiness(self) -> None:
        """calculate the happiness value of each permutation"""
        arrangements = permutations(self._guest_list.keys())
        for group in arrangements:
            self._happiness.append(self._get_happiness(group))

    def happiness(self) -> int:
        """return the object's count"""
        return max(self._happiness)

class Reindeer(object):
    """An object to represent the problem"""
    RACE_TYPES = ['distance', 'points']

    def __init__(self, data:list, race_type:str='distance', 
                 race_time:int=2503) -> None:
        self._reindeer_list = {}
        self._race_type = race_type
        self._race_time = race_time
        self._build_reindeer_list(data)

        if race_type == self.RACE_TYPES[1]:
            self._points = {}
            for deer in self._reindeer_list:
                self._points[deer] = 0

            for _ in range(self._race_time):
                for deer in self._reindeer_list:
                    self._run_race(deer)

                furthest_distance = -1
                leader = None

                for deer in self._reindeer_list:
                    distance = self._reindeer_list[deer][3]
                    if distance >= furthest_distance:
                        furthest_distance = distance
                        leader = deer
                self._points[leader] += 1
        else:
            for deer in self._reindeer_list:
                deer = self._run_race(deer)

    def _build_reindeer_list(self, data:list) -> None:
        """build the dict of reindeer and their running stats"""
        for line in data:
            reindeer, _, _, distance, _, _, duration, *_, rest, _ = line.split()
            flying, secflown, rested = True, 0, 0
            # 0 is for total_distance flown
            self._reindeer_list[reindeer] = [int(distance), int(duration), int(rest), 
                        0, flying, secflown, rested]

    def _run_race(self, deer:list) -> list:
        """
            run the race using the type specified, old rules = distance, new = points
            if self._race_type is not in self.RACE_TYPES, run a distance race
        """
        (distance, duration, rest, distance_flown, 
         flying, secflown, rested) = self._reindeer_list[deer]

        if (self._race_type == self.RACE_TYPES[0] or 
                self._race_type not in self.RACE_TYPES):
            at_rest = False
            clock = 0
            total_distance = 0

            while clock < self._race_time:
                if at_rest:
                    at_rest = not at_rest
                    clock += rest
                else:
                    at_rest = not at_rest
                    clock += duration
                    total_distance += distance * duration
            self._reindeer_list[deer][3] = total_distance
            
        else:
            if flying:
                if secflown == duration:
                    flying = False
                    rested = 1
                else:
                    secflown += 1
                    distance_flown += distance
            else:
                if rested == rest:
                    flying = True
                    secflown = 1
                    distance_flown += distance
                else:
                    rested += 1
            self._reindeer_list[deer][3] = distance_flown
            self._reindeer_list[deer][4] = flying
            self._reindeer_list[deer][5] = secflown
            self._reindeer_list[deer][6] = rested
            
    def winner(self) -> int:
        """return the object's count"""
        if self._race_type == self.RACE_TYPES[0]:
            deer = max(self._reindeer_list, key=lambda x:self._reindeer_list[x][3])
            return f"{deer}, {self._reindeer_list[deer][3]}"
        else:
            deer = max(self._points, key=lambda x:self._points[x])
            return f"{deer}, {self._points[deer]}"

class Cookie(object):
    """An object to represent the problem"""
    MAX_TSP = 100

    def __init__(self, ingredients:str) -> None:
        self._score = 0
        self._500calscore = 0
        self._ingredients = {}
        self._fill_ingredients(ingredients)
        self._optimize()

    def _fill_ingredients(self, ingredients:list) -> None:
        """add the ingredients to the dict"""
        for line in ingredients:
            name, properties = line.split(': ')
            properties = [p.strip() for p in properties.split(',')]
            self._ingredients[name] = {}
            for prop in properties:
                self._ingredients[name][prop.split()[0]] = int(prop.split()[1])

    def _random_partition(self, sum_value:int, num_values:int) -> list:
        """
            returns a set of num_values that sum to sum_value
            ex. random_partition(100, 4) -> [37, 26, 28, 27]
            source: https://stackoverflow.com/a/10287192/2335982
        """
        partition = [0] * num_values
        for _ in range(sum_value):
            partition[random.randrange(num_values)] += 1
        return partition
    
    def _optimize(self) -> None:
        """find the optimal ingredient combination"""
        
        for _ in range(self.MAX_TSP * 1000): # run extra loops to cover randomness
            teaspoons = self._random_partition(self.MAX_TSP, len(self._ingredients))
            capacity, durability, flavor, texture, calories = 0, 0, 0, 0, 0
            for i in range(len(teaspoons)):
                calories += \
                    list(self._ingredients.values())[i]['calories'] * teaspoons[i]
                capacity += \
                    list(self._ingredients.values())[i]['capacity'] * teaspoons[i]
                durability += \
                    list(self._ingredients.values())[i]['durability'] * teaspoons[i]
                flavor += \
                    list(self._ingredients.values())[i]['flavor'] * teaspoons[i]
                texture += \
                    list(self._ingredients.values())[i]['texture'] * teaspoons[i]
            total_score = prod([capacity, durability, flavor, texture])
            if total_score > self._score:
                self._score = total_score
            if calories == 500 and total_score > self._500calscore:
                self._500calscore = total_score
        
    def score(self) -> int:
        """return the best cookie score"""
        return self._score
    
    def score_500cal(self) -> int:
        """return the best 500 calorie cookie score"""
        return self._500calscore

