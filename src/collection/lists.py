def nested_sum(li):
    """
    对制定的列表求和
    :param li:
    :return: 列表的和
    """
    num = 0
    print(type(li))
    for item in li:
        num += sum(item)
    return num


def cumsum(li):
    """
    接收一个数字的列表，返回累计和；也就是说，返回一个新的列表，其中第i
    个元素是原先列表的前i+1个元素的和，
    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]”
    :param li: 数字的列表
    :return: 累加和
    """
    arr = list()
    for i in range(len(li)):
        arr.append(sum(li[:i + 1]))
    return arr


def middle(li):
    """
    接收一个列表作为形参，并返回一个新列表，包含除了第一个和最后一个元素之外的所有元素。例如：
    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]
    :return:
    """
    newArr = list(li)
    newArr.pop(0)
    newArr.pop(len(newArr) - 1)
    return newArr


def chop(li):
    """
    接收一个列表，修改它，删除它的第一个和最后一个元素，并返回None。例如：
    >>> t = [1, 2, 3, 4]
    >>> chop(t)
    >>> t
    [2, 3]
    :param li:
    :return:
    """
    li.pop(0)
    li.pop(len(li) - 1)
    return None


li = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(li))

t = [1, 2, 3, 4]
print(cumsum(t))

print(middle(t))

chop(t)
print(t)