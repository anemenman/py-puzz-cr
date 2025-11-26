"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the
top-3 most occurring words, in descending order of the number of occurrences.

Assumptions:
A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty
 array if a text contains no words.
Examples:
"In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."

--> ["a", "of", "on"]


"e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"

--> ["e", "ddd", "aa"]


"  //wont won't won't"

--> ["won't", "wont"]
Bonus points (not really, but just for fun):
Avoid creating an array whose memory footprint is roughly as big as the input text.
Avoid sorting the entire array of unique words.
"""
import re
from collections import Counter


def top_3_words_v2(text):
    normalized_text = re.sub(r"[^a-zA-Z0-9' ]+", ' ', text).lower()
    if re.search(r"[a-zA-Z0-9]+", normalized_text) is None:
        return []

    words = normalized_text.split()
    word_count = Counter(words)
    top_words = word_count.most_common(3)

    return [word for word, count in top_words]


def top_3_words(text):
    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
    top_3 = Counter(words).most_common(3)
    return [tup[0] for tup in top_3]


text_1 = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income."
assert top_3_words(text_1) == ["a", "of", "on"]

text_2 = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
assert top_3_words(text_2) == ["e", "ddd", "aa"]

text_3 = "//wont won't won't"
assert top_3_words(text_3) == ["won't", "wont"]

assert top_3_words("'") == []
assert top_3_words("'''") == []
