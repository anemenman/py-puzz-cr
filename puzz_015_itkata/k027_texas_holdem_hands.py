"""
Texas Hold'em Hands

Description
Texas Hold'em is a Poker variant in which each player is given two "hole cards". Players then proceed to make a series
of bets while five "community cards" are dealt. If there are more than one player remaining when the betting stops,
a showdown takes place in which players reveal their cards. Each player makes the best poker hand possible using five
of the seven available cards (community cards + the player's hole cards).

Hands
Possible hands are, in descending order of value:

Straight-flush (five consecutive ranks of the same suit). Higher rank is better.
Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank, then the rank of the remaining card.
Full house (three cards with the same rank, two with another). Tiebreaker is first the rank of the three cards, then
rank of the pair.
Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
Straight (five consecutive ranks). Higher rank is better.
Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards, then the highest other
rank, then the second highest other rank.
Two pair (two cards of the same rank, two cards of another rank). Tiebreaker is first the rank of the high pair, then
the rank of the low pair and then the rank of the remaining card.
Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.
Nothing. Tiebreaker is the rank of the cards from high to low.
Task
Given hole cards and community cards, complete the function hand to return the type of hand (as written above, you can
ignore case) and a list of ranks in decreasing order of significance, to use for comparison against other hands of the
same type, of the best possible hand.

hand(["A♠", "A♦"], ["J♣", "5♥", "10♥", "2♥", "3♦"])
# ...should return ("pair", ["A", "J", "10", "5"]})
hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])
# ...should return ("flush", ["Q", "J", "10", "5", "3"])
Notes
This section outlines some deviations from standard Texas Hold'em terminology and rules for those already familiar
with the game.

For straights (and straight flushes) involving an Ace, only the ace-high straight (10-J-Q-K-A) is considered valid. An
ace-low straight (A-2-3-4-5) is not recognized in this rule set, which deviates from the standard Texas Hold'em rules
where both ace-high and ace-low straights are accepted. This interpretation is consistent with the author's reference
solution.
~docgunthrop
In this kata, a Royal Flush is recognized as an Ace-high Straight Flush. The traditional distinction of Royal Flush as
a separate highest hand is not applied here.
The term Nothing corresponds to High Card in standard poker terminology.
"""


def hand(hole_cards, community_cards):
    suits = '♥♦♣♠'
    cards = {k: [0, ''] for k in (*'AKQJ', '10', *'98765432')}
    for c in hole_cards + community_cards:
        cards[c[:-1]][0] += 1
        cards[c[:-1]][1] += c[-1]
    for i in range((lk := len(keys := list(cards.keys()))) - 4):
        s = [set(cards[keys[i + j]][1]) for j in range(5)]
        if all(s) and len(s[0].intersection(*s[1:])) == 1:
            return 'straight-flush', [keys[i + j] for j in range(5)]
    same_ranks = lambda n, i: [c for _ in range(lk) if cards[(c := keys[_])][0] >= n and (not i or c not in i)]
    other_ranks = lambda n, i: [c for _ in range(lk) if cards[(c := keys[_])][0] > 0 and c not in i][:n]
    flush = lambda x: [c for _ in range(lk) if (s := cards[(c := keys[_])])[0] > 0 and x in s[1]][:5]
    if f := same_ranks(4, []):
        return 'four-of-a-kind', f + other_ranks(1, f)
    if f := same_ranks(3, []):
        if s := same_ranks(2, [f[0]]):
            return 'full house', [f[0], s[0]]
    for s in suits:
        if len(f := flush(s)) >= 5:
            return 'flush', f
    for i in range((lk := len(keys)) - 4):
        if all([cards[keys[i + j]][1] for j in range(5)]):
            return 'straight', [keys[i + j] for j in range(5)]
    if f := same_ranks(3, []):
        return 'three-of-a-kind', f + other_ranks(2, f)
    if f := same_ranks(2, []):
        if s := same_ranks(2, [f[0]]):
            return 'two pair', [f[0], s[0]] + other_ranks(1, [f[0], s[0]])
    if f := same_ranks(2, []):
        return 'pair', f + other_ranks(3, f)
    return 'nothing', other_ranks(5, [])


assert hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]) == ("nothing", ["A", "K", "Q", "J", "9"])
assert hand(["A♠", "2♦"], ["3♣", "4♥", "5♥", "7♥", "8♦"]) == ("nothing", ["A", "8", "7", "5", "4"])
assert hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]) == ("pair", ["Q", "K", "J", "9"])
assert hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]) == ("two pair", ["K", "J", "9"])
assert hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]) == ("three-of-a-kind", ["Q", "J", "9"])
assert hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]) == ("straight", ["K", "Q", "J", "10", "9"])
assert hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]) == ("flush", ["Q", "J", "10", "5", "3"])
assert hand(["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"]) == ("full house", ["A", "K"])
assert hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]) == ("four-of-a-kind", ["2", "3"])
assert hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]) == ("straight-flush", ["J", "10", "9", "8", "7"])
