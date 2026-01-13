"""
Prime Streaming (PG-13)

Create an endless generator that yields prime numbers. the generator must be able to produce a million primes in a few
seconds
"""


class Primes:
    @staticmethod
    def stream():
        D = {}
        q = 2
        while True:
            if q not in D:
                yield q
                D[q * q] = [q]

            else:
                for p in D[q]:
                    D.setdefault(p + q, []).append(p)
                del D[q]

            print(D)
            q += 1


gen = Primes.stream()
for _ in range(10):
    print(next(gen))
