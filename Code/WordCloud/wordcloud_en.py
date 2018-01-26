# --coding:utf-8--

from wordcloud import WordCloud
import matplotlib.pyplot as plt

#f = open(u'txt/AliceEN.txt','r').read()
f = """RELION (for REgularised LIkelihood OptimisatioN, pronounce rely-on) is a stand-alone computer program that employs an empirical Bayesian approach to refinement of (multiple) 3D reconstructions or 2D class averages in electron cryo-microscopy (cryo-EM). It is developed in the group of Sjors Scheres at the MRC Laboratory of Molecular Biology. Briefly, the ill-posed problem of 3D-reconstruction is regularised by incorporating prior knowledge: the fact that macromolecular structures are smooth, i.e. they have limited power in the Fourier domain. In the corresponding Bayesian framework, many parameters of a statistical model are learned from the data, which leads to objective and high-quality results without the need for user expertise. The underlying theory is given in Scheres (2012) JMB. A more detailed description of its implementation is given in Scheres (2012) JSB.

As the resolution revolution in cryo-EM progresses, many new software solutions are appearing for which the source code is closed and/or which are not free to use for everyone. The development of RELION is supported through long-term funding by the UK Medical Research Council, and we are proud to distribute RELION under a GPLv2 license. This means that anyone (including commercial users) can download, use and modify RELION without having to pay us anything. If RELION is useful in your work, please do cite our papers about it.

For examples of how we have used RELION, and for a complete list of publications about it, please see our web site. "
"""

wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(f)


# width,height,margin可以设置图片属性

# generate 可以对全部文本进行自动分词,但是他对中文支持不好,对中文的分词处理请看我的下一篇文章
#wordcloud = WordCloud(font_path = r'D:\Fonts\simkai.ttf').generate(f)
# 你可以通过font_path参数来设置字体集

#background_color参数为设置背景颜色,默认颜色为黑色


plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#wordcloud.to_file('test.png')
# 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存