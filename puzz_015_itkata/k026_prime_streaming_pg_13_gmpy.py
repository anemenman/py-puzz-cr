import gmpy2


class Primes:
    @staticmethod
    def stream():
        n = 2
        while True:
            yield n
            n = gmpy2.next_prime(n)


gen = Primes.stream()
for _ in range(10):
    print(next(gen))
