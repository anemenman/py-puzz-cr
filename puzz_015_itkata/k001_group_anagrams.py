"""
star and tsar are anagram of each other because you can rearrange the letters for star to obtain tsar.

Example
A typical test could be :

// input
["tsar", "rat", "tar", "star", "tars", "cheese"]

// output
[
  ["tsar", "star", "tars"],
  ["rat", "tar"],
  ["cheese"]
]
"""


def group_anagrams(words):
    anagram_map = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]

    return list(anagram_map.values())


input_words = ["tsar", "rat", "tar", "star", "tars", "cheese"]

print(group_anagrams(input_words))

print(sorted('bca'))

# import codewars_test as test
# from solution import group_anagrams
#
# sort = lambda a: sorted(sorted(x) for x in a)
#
#
# def dotest(actual, expected):
#     test.assert_equals(sort(actual), sort(expected))
#
#
# @test.describe("Tests")
# def test_group():
#     @test.it("Sample tests")
#     def test_case():
#         dotest(group_anagrams(["rat", "tar", "star"]), [["rat", "tar"], ["star"]])
