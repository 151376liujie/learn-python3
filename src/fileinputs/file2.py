import os

print(__file__)

# 获取当前文件所在的文件目录（绝对路径）
print(os.path.dirname(__file__))

with open("fileinputs.py", 'r') as f:
    read = f.read()
    print(read)