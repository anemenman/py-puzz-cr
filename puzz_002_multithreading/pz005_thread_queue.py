import threading
import queue
import time

"""
queue.Queue is a thread-safe queue in Python that is used to transfer data between threads. 
It avoids thread races and manages synchronization of data access between threads without the need to use Lock.
"""


class ProducerConsumer:
    def __init__(self, num_consumers: int = 5, num_elements: int = 10):
        self.q = queue.Queue()
        self.producer_thread = threading.Thread(target=self._producer)
        self.consumer_threads = (threading.Thread(target=self._consumer) for _ in range(num_consumers))
        self.num_elements = num_elements

    def _producer(self):
        for i in range(self.num_elements):
            self.q.put(i)  # Add to queue
            print(f'Added {i}')
            time.sleep(0.1)  # fake work

    def _consumer(self):
        while not self.q.empty():
            item = self.q.get()  # Get
            print(f'Get {item}')
            self.q.task_done()  # mark done
            time.sleep(0.2)  # fake work

    def run(self):
        self.producer_thread.start()
        time.sleep(0.5)  # fake work

        for t in self.consumer_threads:
            t.start()

        self.producer_thread.join()  # wait to finish producer
        self.q.join()  # wait for all elements


if __name__ == '__main__':
    pc = ProducerConsumer()
    pc.run()
