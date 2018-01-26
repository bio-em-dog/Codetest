# --coding:utf-8--
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = 'ada sda asd adasda aasd asd d as dda s das as da s'

word = jieba.cut(text)

wordcloud = WordCloud(background_color="white").generate(text)

plt.figure()
plt.imshow(wordcloud,interpolation="bilinear")
plt.axis("off")
plt.show()
