import threading

"""
Build a class that will change the value of a counter by incrementing it, run the program on 10 threads 
and 1 million operations for each, and print the result to the screen. The expected value is 10,000,000
"""


class Counter:
    def __init__(self):
        self.value = 0

    def increase(self):
        self.value += abs(1)


def work(counter: Counter, operations_count: int):
    for _ in range(operations_count):
        counter.increase()


def run_threads(counter: Counter, count: int, operations_count: int):
    threads = []

    for _ in range(count):
        t = threading.Thread(target=work, args=(counter, operations_count))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()


if __name__ == '__main__':
    threads_count = 10
    operations_per_thread_count = 1_000_000

    counter = Counter()
    run_threads(counter, threads_count, operations_per_thread_count)

    excepted_result = threads_count * operations_per_thread_count
    actual_result = counter.value
    print(f'Expected result: {excepted_result}, Actual result: {actual_result}')
