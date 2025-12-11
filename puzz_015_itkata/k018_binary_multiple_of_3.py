"""
In this kata, your task is to create a regular expression capable of evaluating binary strings (strings with only 1s
and 0s) and determining whether the given string represents a number divisible by 3.

Take into account that:
An empty string might be evaluated to true (it's not going to be tested, so you don't need to worry about it - unless
you want)
The input should consist only of binary digits - no spaces, other digits, alphanumeric characters, etc.
There might be leading 0s.
Examples (Javascript)
multipleof3Regex.test('000') should be true
multipleof3Regex.test('001') should be false
multipleof3Regex.test('011') should be true
multipleof3Regex.test('110') should be true
multipleof3Regex.test(' abc ') should be false
You can check more in the example test cases

Note
There's a way to develop an automata (FSM) that evaluates if strings representing numbers in a given base are divisible
by a given number. You might want to check an example of an automata for doing this same particular task here.

If you want to understand better the inner principles behind it, you might want to study how to get the modulo of an
arbitrarily large number taking one digit at a time.
"""

import re

"""
DFA mod 3 = 0

    0                    1
   __                    __
   | |                   | |
   | v   1          0    | v
-> q0 -------> q1 ------> q2 
      <-------    <------
          1          0
          
"""

# PATTERN = re.compile(r'^(1(01*0)*1|0)*$')
PATTERN = re.compile(r'^(0*(1(01*0)*1)*)*$')

assert not bool(PATTERN.match(' 0'))
assert not bool(PATTERN.match('abc'))
assert bool(PATTERN.match('000'))
assert bool(PATTERN.match('110'))
assert not bool(PATTERN.match('111'))
assert bool(PATTERN.match("{:b}".format(12345678)))
