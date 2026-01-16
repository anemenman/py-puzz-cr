"""
Prime Streaming (PG-13)

Create an endless generator that yields prime numbers. the generator must be able to produce a million primes in a few
seconds
"""
import itertools


class Primes:
    @staticmethod
    def stream():
        yield 2
        D = {}
        for q in itertools.count(3, step=2):
            p = D.pop(q, None)
            if not p:
                D[q * q] = q
                yield q
            else:
                x = q + p + p
                while x in D:
                    x += p + p
                D[x] = p


gen = Primes.stream()
for _ in range(10):
    print(next(gen))
