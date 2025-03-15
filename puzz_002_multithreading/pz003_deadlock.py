import threading

"""
1) thread acquires self.lock in outer_method();
2) inner_method() is called, which also tries to acquire self.lock, but it is already locked by the same thread;
3) Python blocks execution because Lock does not allow re-acquiring by the same thread.
"""


class DeadLockExample:
    def __init__(self):
        self.lock = threading.Lock()

    def outer_method(self):
        with self.lock:
            print('External method was blocked')
            self.inner_method()

    def inner_method(self):
        with self.lock:
            print('Internal method was blocked')


example = DeadLockExample()
thread = threading.Thread(target=example.outer_method)
thread.start()
thread.join()
