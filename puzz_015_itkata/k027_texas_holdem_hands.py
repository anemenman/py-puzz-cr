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

from itertools import combinations, groupby

RANK_ORDER = '23456789TJQKA'
RANKS = {r: i for i, r in enumerate(RANK_ORDER, 2)}
print(RANKS)
REVERSE_RANKS = {i: r for r, i in RANKS.items()}
print(REVERSE_RANKS)
SUITS = '♠♣♥♦'


def parse(card):
    """Parses card string like 'A♠' to ('A', '♠')"""
    return (card[:-1], card[-1])


def hand(hole, community):
    cards = [parse(c) for c in hole + community]
    best = None
    best_type = None
    best_key = None
    for cmb in combinations(cards, 5):
        ttype, tkey = eval_hand(cmb)
        if best is None or hand_rank(ttype, tkey) > hand_rank(best_type, best_key):
            best_type = ttype
            best_key = tkey
    return best_type, [REVERSE_RANKS[k] for k in best_key]


def eval_hand(cards):
    # cards: list of 5 (rank, suit)
    ranks = [RANKS[r] for r, s in cards]
    suits = [s for r, s in cards]
    counts = {r: ranks.count(r) for r in set(ranks)}
    groups = sorted(((cnt, r) for r, cnt in counts.items()), reverse=True)  # by count, then by rank
    ranks_sorted = sorted(ranks, reverse=True)
    flush = False
    straight = False
    straight_high = None

    # Check Flush
    fsuits = [s for s in suits if suits.count(s) == 5]
    if fsuits:
        flush = True

    # Check Straight
    uniq_ranks = sorted(set(ranks), reverse=True)
    if len(uniq_ranks) >= 5:
        # Only allow A-high straight (T,J,Q,K,A)
        if uniq_ranks == [14, 13, 12, 11, 10]:
            straight = True
            straight_high = 14
        else:
            for i in range(len(uniq_ranks) - 4):
                window = uniq_ranks[i:i + 5]
                if all(window[j] - 1 == window[j + 1] for j in range(4)):
                    straight = True
                    straight_high = window[0]
                    break

    # Check Straight Flush
    if flush and straight:
        # pick all same-suit cards and check straight there
        for suit in SUITS:
            suited = [RANKS[r] for r, s in cards if s == suit]
            uniq_suited = sorted(set(suited), reverse=True)
            if len(uniq_suited) >= 5:
                if uniq_suited == [14, 13, 12, 11, 10]:
                    return "straight-flush", [14]
                for i in range(len(uniq_suited) - 4):
                    wnd = uniq_suited[i:i + 5]
                    if all(wnd[j] - 1 == wnd[j + 1] for j in range(4)):
                        return "straight-flush", [wnd[0]]

    # Four of a kind
    if groups[0][0] == 4:
        quad = groups[0][1]
        kicker = max([k for k in ranks if k != quad])
        return "four-of-a-kind", [quad, kicker]
    # Full house
    if groups[0][0] == 3 and groups[1][0] == 2:
        return "full house", [groups[0][1], groups[1][1]]
    # Flush
    if flush:
        f_suit = fsuits[0]
        f_cards = [RANKS[r] for r, s in cards if s == f_suit]
        top5 = sorted(f_cards, reverse=True)[:5]
        return "flush", top5
    # Straight
    if straight:
        return "straight", [straight_high]
    # Three of a kind
    if groups[0][0] == 3:
        trips = groups[0][1]
        kickers = sorted([k for k in ranks if k != trips], reverse=True)[:2]
        return "three-of-a-kind", [trips] + kickers
    # Two pair
    if groups[0][0] == 2 and groups[1][0] == 2:
        pair1 = max(groups[0][1], groups[1][1])
        pair2 = min(groups[0][1], groups[1][1])
        kicker = max([k for k in ranks if k != pair1 and k != pair2])
        return "two pair", [pair1, pair2, kicker]
    # Pair
    if groups[0][0] == 2:
        pair = groups[0][1]
        kickers = sorted([k for k in ranks if k != pair], reverse=True)[:3]
        return "pair", [pair] + kickers
    # Nothing
    return "nothing", ranks_sorted[:5]


def hand_rank(ttype, tkey):
    order = ['nothing', 'pair', 'two pair', 'three-of-a-kind', 'straight', 'flush',
             'full house', 'four-of-a-kind', 'straight-flush']
    return (order.index(ttype), tkey)


# Примеры из задачи
# r1 = hand(["A♠", "A♦"], ["J♣", "5♥", "10♥", "2♥", "3♦"])
# r2 = hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])

print(hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]))
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
