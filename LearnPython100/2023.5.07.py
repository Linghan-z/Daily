#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : 2023.5.07.py
# @Time    : 5/7/23 21:00
# @Author  : zlhhh
# @Description :
import numpy as np
import pandas as pd


def euclidean_distance(x, y):
    x = np.array(x)
    y = np.array(y)
    # return np.around(np.sqrt(np.sum(np.square(x - y))), 3)
    return np.sqrt(np.sum(np.square(x - y)))


def manhattan_distance(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.around(np.sum(np.abs(x - y)), 3)


def chebyshev_distance(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.around(np.max(np.abs(x - y)), 3)


def cosine_similarity(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.around(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y)), 8)


def norm(x):
    x = np.array(x)
    a = np.linalg.norm(x)
    return (x / a)


def calculation(x, y):
    print(y, "euclidean distance: ", euclidean_distance(x, y),
          "\n manhattan_distance: ", manhattan_distance(x, y),
          "\n chebyshev_distance: ", chebyshev_distance(x, y),
          "\n cosine_similarity: ", cosine_similarity(x, y))


def min_max_scaler(data):
    scaler = (data - data.min()) / (data.max() - data.min())
    return scaler


# 标准差标准化
def standard_scaler(data):
    print(data.std(ddof=0))
    data = (data - data.mean()) / data.std(ddof=0)
    print(data)
    return data


def standard_scaler_mean_abs_dev(data):
    mean = data.mean()
    mad = np.mean(np.abs(data - mean))
    return (data - mean) / mad
    # data = (data - data.mean())/np.mean(np.abs(data - mean))


# 小数定标规范化
def decimal_scaler(data):
    data = data / 10 ** np.ceil(np.log10(data.abs().max()))
    return data


def main():
    # x = [1.4, 1.6]
    # # x1 = [1.5, 1.7]
    # # x2 = [2, 1.9]
    # # x3 = [1.6, 1.8]
    # # x4 = [1.2, 1.5]
    # # x5 = [1.5, 1.0]
    # y = [[1.5, 1.7], [2, 1.9], [1.6, 1.8], [1.2, 1.5], [1.5, 1.0]]
    # z = []
    # for item in y:
    #     # calculation(x, item)
    #
    #     z.append(norm(item))
    # # print(z)
    # x_norm = norm(x)
    # print(x_norm)
    # for item in z:
    #     print(euclidean_distance(x_norm, item))

    data = [200, 300, 400, 600, 1000]
    ser1 = pd.Series(data)
    # print(ser1)
    # print(min_max_scaler(ser1))
    # print(standard_scaler(ser1))
    print(decimal_scaler(ser1))
    # print(standard_scaler_mean_abs_dev(ser1))


if __name__ == '__main__':
    main()

# class Count:
#     def __init__(self, name, count):
#         self.name = name
#         self.count = count
#
# schema = {...}  # 数据集结构定义，例如 {"name": str, "age": int, "city": str}
# data = [...]  # 数据集，例如 [{"name": "Alice", "age": 25, "city": "New York"}, {...}]
# count_ary = []  # 用于保存属性的不同值计数
#
# def count_distinct(attribute):
#     distinct_values = set()
#     for record in data:
#         distinct_values.add(record[attribute])
#     return len(distinct_values)
#
# for attribute in schema:
#     distinct_count = count_distinct(attribute)
#     count_obj = Count(attribute, distinct_count)
#     count_ary.append(count_obj)
#
# # 按count升序对ary []进行排序；
# count_ary.sort(key=lambda x: x.count)
#
# concept_hierarchy = []
# for count_obj in count_ary:
#     # 生成概念层次结构节点
#     concept_hierarchy.append(count_obj.name)

# 用于生成概念层次结构的数值属性
concept_attb = ""


# 表示概念层次结构（作为值的有序列表）
class Concept:
    def __init__(self, name, min, max):
        self.name = name
        self.min = min
        self.max = max
        self.mean = 0
        self.sum = 0
        self.count = 0


concept_hierarchy = []

# 用户指定的最小数据值、最大数据值、箱的宽度
range_min = 0
range_max = 100
step = 10
j = 0

# 初始化概念层次结构数组
for i in range(range_min, range_max, step):
    concept = Concept("level_" + str(j), i, i + step - 1)
    concept_hierarchy.append(concept)
    j += 1

# 必要时初始化最终最大值
if i + step - 1 >= range_max:
    concept = Concept("level_" + str(j), i + step - 1, range_max)
    concept_hierarchy.append(concept)

# 通过增加适当的总和和计数值，将每个值分配给箱
for tuple_T in task_relevant_data_set:
    k = 0
    while tuple_T[concept_attb] > concept_hierarchy[k].max:
        k += 1
    concept_hierarchy[k].sum += tuple_T[concept_attb]
    concept_hierarchy[k].count += 1

# 计算用于表示每个级别值的箱度量
# 在概念层次结构中
for concept in concept_hierarchy:
    if concept.count != 0:
        concept.mean = concept.sum / concept.count
