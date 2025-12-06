from collections import defaultdict, OrderedDict

if __name__ == '__main__':
    map = defaultdict(list)
    map[1] = [1, 2, 3]
    map[2] = [4, 5, 6]

    print(map)
    print(map['3'])
    print(map.__contains__('3'))

    li = [1,2,3]
    li2 = {1,2,3}
    print(type(li))
    print(type(li2))
