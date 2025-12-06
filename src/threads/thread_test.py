import threading
import time


def fun1(*args):
    while True:
        print(threading.current_thread().name + " is running~")
        time.sleep(2)
        break


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=fun1, args=())
        t.name = "thread-%d" % i
        t.daemon = False
        t.start()
    else:
        print("main thread done.")
        a = 1
        if a == 1:
            print("asdfasd")
