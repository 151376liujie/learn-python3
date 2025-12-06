fin = open("/Users/liujie/PycharmProjects/learn-python3/src/string/words.txt")


def printEachLine():
    """
    打印文件中的每一行
    :return: void
    """
    for row in fin:
        r = row.strip()
        if len(r) > 20:
            print(r)


def has_no_e(word):
    """
    “当给定的单词不包含字母“e”时，返回True
    :param word: 给定的单词
    :return: Ture如果给定单词中不含字母e；否则返回False
    """
    if 'e' in word:
        return False
    return True


def avoids(word, forbidden):
    """
    “接收一个单词，以及一个包含禁止字母的字符串，当单词不含任何禁止字母时，返回True”
    :param word: 给定的单词
    :param forbidden: 禁止字母的字符串
    :return: 当单词不含任何禁止字母时,返回True
    """
    for ch in forbidden:
        if ch in word:
            return False
    return True


def uses_all(word, chs):
    """
    “接收一个单词以及由需要的字母组成的字符串，当单词中所有需要的字母都出现了至少一次时返回True
    :param word: 给定单词
    :param chs: 需要的字母组成的字符串
    :return:
    """
    for ch in chs:
        if ch not in word:
            return False
    return True


def abecedarian(word):
    """
    “如果单词中的字母是按照字母表顺序排列的（两个重复字母也可以），则返回True”
    :param word:  给定的单词
    :return: True如果给定的单词是按照字母表顺序排列的，否则返回False
    """
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


# print(avoids('words', 'sd'))
# print(avoids('words', 'hk'))
for line in fin:
    # if uses_all(line.strip(), 'aeiou'):
    #     print(line.strip())
    if abecedarian(line.strip()):
        print(line.strip())
