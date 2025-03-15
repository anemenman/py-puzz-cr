import threading

"""
Fix for pz003_deadlock.py with threading.RLock()
"""


class NoDeadLockExample:
    def __init__(self):
        self.lock = threading.RLock()

    def outer_method(self):
        with self.lock:
            print('External method was blocked')
            self.inner_method()

    def inner_method(self):
        with self.lock:
            print('Internal method was blocked')


example = NoDeadLockExample()
thread = threading.Thread(target=example.outer_method)
thread.start()
thread.join()
