#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : Loltrain.py
# @Time    : 6/26/23 21:32
# @Author  : zlhhh
# @Description :

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 加载数据集
df = pd.read_csv('datamining.csv')

# 去除冗余特征
features = ['blueWardsPlaced', 'blueWardsDestroyed', 'blueFirstBlood', 'blueKills', 'blueDeaths',
            'blueAssists', 'blueEliteMonsters', 'blueDragons', 'blueHeralds', 'blueTowersDestroyed',
            'blueTotalGold', 'blueAvgLevel', 'blueTotalExperience', 'blueTotalMinionsKilled',
            'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff', 'redWardsPlaced',
            'redWardsDestroyed', 'redAssists', 'redEliteMonsters', 'redDragons', 'redHeralds',
            'redTowersDestroyed', 'redTotalGold', 'redAvgLevel', 'redTotalExperience',
            'redTotalMinionsKilled', 'redTotalJungleMinionsKilled']

df = df[features + ['blueWins']]  # 保留需要的特征

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(df[features], df['blueWins'], test_size=0.3, random_state=42)

'''逻辑回归'''
# 训练逻辑回归模型
lr = LogisticRegression()
lr.fit(X_train, y_train)

# 使用测试集进行预测
y_pred = lr.predict(X_test)

# 计算模型的准确率
acc = accuracy_score(y_test, y_pred)
print(f'The accuracy of the logistic regression model is {acc:.5f}')

'''随机森林'''
# 训练随机森林模型
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 使用测试集进行预测
y_pred = rf.predict(X_test)

# 计算模型的准确率
acc = accuracy_score(y_test, y_pred)
print(f'The accuracy of the random forest model is {acc:.5f}')

'''SVM'''
# 划分训练集和测试集，并进行数据标准化
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(df[features], df['blueWins'], test_size=0.3, random_state=42)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 训练支持向量机模型
svm = SVC(kernel='linear', C=1, random_state=42)
svm.fit(X_train, y_train)

# 使用测试集进行预测
y_pred = svm.predict(X_test)

# 计算模型的准确率
acc = accuracy_score(y_test, y_pred)
print(f'The accuracy of the SVM model is {acc:.5f}')

'''MLP'''
# 划分训练集和测试集，并进行数据标准化
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(df[features], df['blueWins'], test_size=0.3, random_state=42)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 定义 MLP 模型
mlp = MLPClassifier(max_iter=500, early_stopping=True, random_state=42)

# 定义超参数搜索空间
param_grid = {
    'hidden_layer_sizes': [(32,), (64,), (32, 32), (64, 32)],
    'activation': ['relu', 'tanh'],
    'solver': ['adam', 'lbfgs'],
    'learning_rate_init': [0.001, 0.01, 0.1],
}

# 使用网格搜索找到最佳参数组合
grid_search = GridSearchCV(mlp, param_grid=param_grid, cv=5, n_jobs=-1)
grid_search.fit(X_train, y_train)

# 输出最佳参数组合和交叉验证得分
print(f'Best parameters: {grid_search.best_params_}')
print(f'Cross-validation score: {grid_search.best_score_:.2f}')

# 使用测试集进行预测
y_pred = grid_search.predict(X_test)

# 计算模型的准确率
acc = accuracy_score(y_test, y_pred)
print(f'The accuracy of the MLP model is {acc:.2f}')
