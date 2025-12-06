import os

print("current dir is: ", os.path.curdir)
print("parent dir: ", os.path.pardir)
print("current dir name is: ", os.path.dirname(__file__))
abspath = os.path.abspath(__file__)
print("abs path is: ", abspath)
print("base name is: ", os.path.basename(abspath))
print("list dir is: ", os.listdir(os.path.dirname(__file__)))
