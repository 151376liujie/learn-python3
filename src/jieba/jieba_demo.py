import jieba
# jieba中文分词库
# li = jieba.lcut("中华人民共和国", cut_all=True)
li = jieba.lcut("中国是一个伟大的国家")

print(li)
