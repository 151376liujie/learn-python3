import threading
import time
from threading import current_thread

class MyThread(threading.Thread):

    def run(self):
        print(current_thread().name + " is running.")
        time.sleep(1)

t1 = MyThread()
t1.start()
t1.join()

print(current_thread().name + " is running.")