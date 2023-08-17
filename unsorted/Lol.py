#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : Lol.py
# @Time    : 6/26/23 20:20
# @Author  : zlhhh
# @Description :


import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 加载数据集
df = pd.read_csv('../data/datamining.csv')

# 去除冗余特征
features = ['blueWardsPlaced', 'blueWardsDestroyed', 'blueFirstBlood', 'blueKills', 'blueDeaths',
            'blueAssists', 'blueEliteMonsters', 'blueDragons', 'blueHeralds', 'blueTowersDestroyed',
            'blueTotalGold', 'blueAvgLevel', 'blueTotalExperience', 'blueTotalMinionsKilled',
            'blueTotalJungleMinionsKilled', 'blueGoldDiff', 'blueExperienceDiff', 'redWardsPlaced',
            'redWardsDestroyed', 'redAssists', 'redEliteMonsters', 'redDragons', 'redHeralds',
            'redTowersDestroyed', 'redTotalGold', 'redAvgLevel', 'redTotalExperience',
            'redTotalMinionsKilled', 'redTotalJungleMinionsKilled']
df = df[features + ['blueWins']]  # 保留需要的特征

# 划分训练集和测试集，并进行数据标准化
scaler = StandardScaler()
X_train, X_test, y_train, y_test = train_test_split(df[features], df['blueWins'], test_size=0.3, random_state=42)
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)


# 定义数据集类
class MyDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y.values, dtype=torch.float32).view(-1, 1)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]


# 定义训练集和测试集数据加载器
train_set = MyDataset(X_train, y_train)
test_set = MyDataset(X_test, y_test)
train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
test_loader = DataLoader(test_set, batch_size=64)


# 定义ResNet模型
class ResNet(nn.Module):
    def __init__(self, input_dim=29, hidden_dim=16, output_dim=1):
        super(ResNet, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.res1 = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.res2 = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim)
        )
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        shortcut = x
        x = self.res1(x)
        x += shortcut
        x = self.relu(x)
        shortcut = x
        x = self.res2(x)
        x += shortcut
        x = self.relu(x)
        x = self.fc2(x)
        x = nn.Sigmoid()(x)
        return x

# 定义神经网络模型
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(29, 16)
        self.fc2 = nn.Linear(16, 8)
        self.fc3 = nn.Linear(8, 1)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc3(x)
        x = nn.Sigmoid()(x)
        return x


# 定义训练函数
def train(model, train_loader, optimizer, criterion):
    model.train()
    running_loss = 0.0
    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * inputs.size(0)
    train_loss = running_loss / len(train_loader.dataset)
    return train_loss


# 定义测试函数
def test(model, test_loader, criterion):
    model.eval()
    running_loss = 0.0
    y_true = []
    y_pred = []
    with torch.no_grad():
        for inputs, labels in test_loader:
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            running_loss += loss.item() * inputs.size(0)
            y_true.extend(labels.numpy().tolist())
            y_pred.extend(outputs.numpy().flatten().tolist())
    test_loss = running_loss / len(test_loader.dataset)
    test_acc = accuracy_score(y_true, [1 if p >= 0.5 else 0 for p in y_pred])
    return test_loss, test_acc


# 创建模型实例、优化器和损失函数
model = ResNet()
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)
criterion = nn.BCELoss()

# 训练神经网络
for epoch in range(20):
    train_loss = train(model, train_loader, optimizer, criterion)
    print(f"Epoch {epoch + 1}, Train Loss: {train_loss:.4f}")
test_loss, test_acc = test(model, test_loader, criterion)
print(f"Test Loss: {test_loss}, Test Accuracy: {test_acc}")
