import wordcloud
import jieba

wc = wordcloud.WordCloud( width=600, height=400, font_path='/System/Library/Fonts/STHeiti Light.ttc')

f = open("政府工作报告2024.txt", mode='r', encoding='utf-8')
t = f.read()
f.close()

li = jieba.lcut(t)
wc.generate(" ".join(li))

wc.to_file("wordcloud.jpg")
