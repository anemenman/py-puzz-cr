import threading
import time

"""
threading.Condition allows one thread to wait for another thread to complete the required actions. 
It is used when one or more threads depend on a change in state in another thread. 
Waiting threads call wait() until another thread calls notify() or notify_all(). 
This is useful when consumers must wait for a producer to prepare data, or when a data processor 
needs to know that certain conditions have been met. Condition allows you to optimize the interaction 
between threads and avoid active waiting (long polling), stop threads until a certain condition is met, 
and notify them to continue.
"""


class DataPipeline:
    def __init__(self):
        self.data_ready = False
        self.condition = threading.Condition()

    def produce(self):
        with self.condition:
            print('Producer generate the data')
            time.sleep(1)
            self.data_ready = True
            self.condition.notify_all()  # notify that data are ready

    def consume(self):
        with self.condition:
            while not self.data_ready:
                self.condition.wait()  # Wait for notify_all()
            print('Consumer got the data')


pipeline = DataPipeline()
threading.Thread(target=pipeline.consume).start()
threading.Thread(target=pipeline.produce).start()
