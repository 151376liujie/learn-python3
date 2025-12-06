import fileinput
import random
import time

if __name__ == '__main__':
    li = ['/Users/liujie/PycharmProjects/learn-python3/src/beautifulsoups/bs4_test_bak.py']
    for line in fileinput.input(files=li):
        print(line, fileinput.lineno(), fileinput.filelineno())
        # content = line.rstrip()
        # num = fileinput.filelineno()
        # print('{:<50} # {:2d}'.format(content, num))
