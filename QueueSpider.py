import threading
from queue import Queue
import time

class MyThread(threading.Thread):
    def __init__(self,name,lock):
        threading.Thread.__init__(self)
        self.name = name
        self.lock = lock
    def run(self):
        time.sleep(1)
        lock.acquire()
        print(self.name)
        lock.release()

lock = threading.Lock()
q = Queue()
for i in range(10):
    t = MyThread(threading.current_thread().name, lock)
    t.start()
