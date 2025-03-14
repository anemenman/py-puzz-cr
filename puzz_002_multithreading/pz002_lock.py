import threading

"""
See pz001_race_conditions.py
By deciding to use threading.Lock, we guarantee that only one thread is performing the add operation at a given time.
"""


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increase(self):
        with self.lock:
            self.value += 1


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
