"""
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to
a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an
electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another
adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4.
And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally
lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in
Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function
getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results,
must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!
"""
from itertools import product


def get_pins(observed):
    neighbors = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
    }

    def generate_pins(current_pin, remaining_digits):
        if not remaining_digits:
            return [current_pin]

        digit = remaining_digits[0]
        possible_digits = neighbors[digit]
        result = []

        for next_digit in possible_digits:
            result.extend(generate_pins(current_pin + next_digit, remaining_digits[1:]))

        return result

    return generate_pins('', observed)


NEIGHBORS_NUM = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')


def get_pins_v2(observed):
    return [''.join(p) for p in product(*(NEIGHBORS_NUM[int(d)] for d in observed))]


assert sorted(get_pins('8')) == sorted(['5', '7', '8', '9', '0'])
assert sorted(get_pins('11')) == sorted(["11", "22", "44", "12", "21", "14", "41", "24", "42"])
assert sorted(get_pins('369')) == sorted(
    ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398",
     "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359",
     "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"])
assert sorted(get_pins('0')) == sorted(['0', '8'])
