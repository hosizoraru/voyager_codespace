import worldcould as wc
import jieba
import imageio
import networkx as nx
import matplotlib.pyplot as plt
import jieba.posseg as pseg
import random
import codecs
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.charts import Line

MainTop = 20

file = open('threekingdoms.txt', 'r+', encoding='utf-8')
txt = file.read()
file.close()

txt = txt.replace('孔明曰','孔明')
txt = txt.replace('玄德曰','玄德')
txt = txt.replace('玄德','刘备')
txt = txt.replace('关公','云长')
txt = txt.replace('云长','关羽')

ls = jieba.lcut(txt)
excludes = {'不可','却说','二人','不能','次日','左右','主公','于是',
          '今日','天下','大喜','将军','引兵','商议','陛下','都督',
          '不敢','如何','如此','众将','只见','后主','此人','不知',
          '人马','先主','一人','丞相'}

poss = pseg.cut(txt)


