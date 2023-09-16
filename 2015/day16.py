"""
    day16.py
    Advent of Code, 2015
    Day 16: Aunt Sue

    Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank 
    you card. However, there's a small problem: she signed it "From, Aunt Sue".

    You have 500 Aunts named "Sue".

    So, to avoid sending the card to the wrong person, you need to figure out which 
    Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. 
    You open the present and, as luck would have it, good ol' Aunt Sue got you a My 
    First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case 
    may be.

    The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few 
    specific compounds in a given sample, as well as how many distinct kinds of those 
    compounds there are. According to the instructions, these are what the MFCSAM can 
    detect:

        - children, by human DNA age analysis.
        - cats. It doesn't differentiate individual breeds.
        - Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, 
          and vizslas.
        - goldfish. No other kinds of fish.
        - trees, all in one group.
        - cars, presumably by exhaust or gasoline or something.
        - perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

    In fact, many of your Aunts Sue have many of these. You put the wrapping from the 
    gift into the MFCSAM. It beeps inquisitively at you a few times and then prints 
    out a message on ticker tape:

        children: 3
        cats: 7
        samoyeds: 2
        pomeranians: 3
        akitas: 0
        vizslas: 0
        goldfish: 5
        trees: 3
        cars: 2
        perfumes: 1

    Part 1: What is the number of the Sue that got you the gift?
    Part 2: What is the number of the real Aunt Sue?
"""
import sys
from pathlib import Path

from aoc15 import SueSearch

def read_data(file_path: str) -> list:
    """read processing data from the file specified"""
    raw_data = Path(file_path).read_text(encoding='utf-8').strip()
    return [line.strip() for line in raw_data.split('\n')]

if __name__ == '__main__':
    if len(sys.argv[1:]) > 0:
        for path in sys.argv[1:]:
            print(f"\n{path}:")
            data = read_data(path)
            ticker = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, \
                'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, \
                'perfumes': 1
            }
            sue_search = SueSearch(data, ticker)
            print(f'Part 1: {sue_search.ExactSue()}')
            print(f'Part 2: {sue_search.RetroSue()}')
    else:
        # run tests
        print("\nNo unit tests for this solution\n")
