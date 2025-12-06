import os
import shutil
import zipfile


class Bird(object):
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("eating")
            self.hungry = False
        else:
            print("no,thanks!")


class SongBird(Bird):
    def __init__(self):
        super().__init__()
        self.sound = 'Squawk'

    def sing(self):
        print(self.sound)


class Rectange:
    def __init__(self):
        self.height = 0
        self.width = 0

    @property
    def size(self):
        print("get")
        return self.width, self.height

    # def size(self, size):
    #     self.width, self.height = size

    # size = property(_get_size, _set_size)


if __name__ == '__main__':
    r = Rectange()
    r.width = 15
    r.height = 10
    print(r.width)
    print(r.height)
    print(r.size)

    # path = '/Users/liujie/Movies/learnning-center/python/鱼C-python'
    # for dirs in os.listdir(path):
    #     abspath = path + "/" + dirs
    #     if os.path.isdir(abspath):
    #         for subdir in os.listdir(abspath):
    #             subpath = abspath + "/" + subdir
    #             if os.path.isdir(subpath):
    #                 for subsubdir in os.listdir(subpath):
    #                     subsubpath = subpath + "/" + subsubdir
    #                     if subsubdir.endswith(".mp4"):
    #                         shutil.move(subsubpath, path)

    # path = u'/Users/liujie/Movies/learnning-center/python/鱼C-python/028文件：因为懂你，所以永恒.zip'
    # shutil.unpack_archive(path, u'/Users/liujie/Movies/learnning-center/python/鱼C-python/')
    # zipf = zipfile.ZipFile(path, 'r')
    # for name in zipf.namelist():
    #     zipf.extract(name, u'/Users/liujie/Movies/learnning-center/python/鱼C-python/')
