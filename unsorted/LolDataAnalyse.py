#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : LolDataAnalyse.py
# @Time    : 6/26/23 15:39
# @Author  : zlhhh
# @Description :

#  基础函数库
import numpy as np
import pandas as pd

# 绘图函数库
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv('../data/datamining.csv')
# print(df.head())
# print(df.describe())

y = df.blueWins

# 我们可以去除一些重复变量，比如只要知道蓝队是否拿到一血，我们就知道红队有没有拿到，可以去除红队的相关冗余数据。
drop_cols = ['gameId', 'blueWins', 'gameId', 'blueWins', 'redFirstBlood',
             'redKills', 'redDeaths', 'redGoldDiff', 'redExperienceDiff',
             'blueCSPerMin', 'blueGoldPerMin', 'redCSPerMin', 'redGoldPerMin']
X = df.drop(drop_cols, axis=1)

features = ['blueWardsPlaced', 'blueWardsDestroyed', 'blueFirstBlood', 'blueKills', 'blueDeaths',
            'blueAssists', 'blueEliteMonsters', 'blueDragons', 'blueHeralds', 'blueTowersDestroyed',
            'blueTotalGold', 'blueAvgLevel', 'blueTotalExperience', 'blueTotalMinionsKilled',
            'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff', 'redWardsPlaced',
            'redWardsDestroyed', 'redAssists', 'redEliteMonsters', 'redDragons', 'redHeralds',
            'redTowersDestroyed', 'redTotalGold', 'redAvgLevel', 'redTotalExperience',
            'redTotalMinionsKilled', 'redTotalJungleMinionsKilled']
print(len(features))
# df.hist(bins=50, figsize=(20, 15))
# # plt.show()
#
# sns.pairplot(df, hue='blueWins', vars=['blueGoldDiff', 'blueExperienceDiff', 'blueKills', 'blueDeaths', 'blueAssists'],
#              corner=True)
# plt.show()


# # 箱线图
# # 绘制多个子图，每个子图显示一个特征与blueWins之间的关系
# fig, axs = plt.subplots(nrows=6, ncols=5, figsize=(20, 25))
# for i, feature in enumerate(features):
#     row, col = i // 5, i % 5
#     sns.boxplot(x='blueWins', y=feature, data=df, ax=axs[row, col])
#
# # 增加全局标题和子图标题
# fig.suptitle('Relationship between Features and blueWins', fontsize=20)
# for i, ax in enumerate(axs.flat):
#     if i >= len(features):
#         ax.remove()
#     else:
#         ax.set(title=f'{features[i]} vs blueWins', xlabel='', ylabel='')
# # 显示图像
# plt.show()

# 小提琴图
# 创建一个包含所有特征的子图网格
fig, axs = plt.subplots(nrows=6, ncols=5, figsize=(20, 25))
# 遍历每个特征，绘制对应的小提琴图
for i, feature in enumerate(features):
    row, col = i // 5, i % 5
    sns.violinplot(x='blueWins', y=feature, data=df, ax=axs[row, col], palette='husl')

# 增加全局标题和子图标题
fig.suptitle('Relationship between Features and blueWins', fontsize=20)
for i, ax in enumerate(axs.flat):
    if i >= len(features):
        ax.remove()
    else:
        ax.set(title=f'{features[i]} vs blueWins', xlabel='', ylabel='')

# 显示图像
plt.show()

