#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : chimerge.py
# @Time    : 5/8/23 15:27
# @Author  : zlhhh
# @Description :
import numpy as np

filename = '../data/iris.data'


# 读取数据
def read_data(filename):
    with open(filename, 'r') as f:
        content = f.read()
    iris_list = content.strip().split('\n')
    return iris_list


# 鸢尾花4个属性值列表
# sepal_length = []
# sepal_width = []
# petal_length = []
# petal_width = []
def initial_interval(iris_list, attribute_num):
    """
    :param iris_list: data
    :param attribute_num: 0-->sepal_length; 1-->sepal_width; 2-->petal_length; 3-->petal_width
    :return: 排序后的某属性值与当前类别信息元组
    """
    attribute = []
    for value in iris_list:
        temp_list = value.strip().split(",")
        initial_set = {"interval": []}  # 创建字典用来储存属性区间的元素(属性数值)
        initial_set["interval"].append(temp_list[attribute_num])

        # 定义一个空元组用来储存类别信息，'Iris-setosa'-> (1,0,0), 'Iris-versicolor'-> (0,1,0), 'Iris-virginica' -> (0,0,1)
        if temp_list[4] == 'Iris-setosa':
            class_tuple = [1, 0, 0]
        if temp_list[4] == 'Iris-versicolor':
            class_tuple = [0, 1, 0]
        if temp_list[4] == 'Iris-virginica':
            class_tuple = [0, 0, 1]
        interval_class = (initial_set, class_tuple)  # 储存当前属性值与类别信息
        attribute.append(interval_class)  # 相同属性整合在一个列表中
        attribute.sort(key=lambda x: x[0]["interval"][0])  # 按属性值大小排序
    return attribute


def chi2(A, B):
    """卡方计算"""
    table = np.array([A, B])
    e_ij = 0
    sum_chi2 = 0
    for i in range(2):
        for j in range(len(A)):
            e_ij = np.sum(table[:, j]) * np.sum(table[i, :]) / np.sum(table)
            if e_ij != 0:
                sum_chi2 += (table[i][j] - e_ij) ** 2 / e_ij
    return sum_chi2


def merge(interval_1, interval_2):
    """
    合并相邻区间，前半部分（数值）append，后半部分（类型）相加
    :param interval_1: 区间1
    :param interval_2: 区间2
    :return: interval_1
    """
    for value in interval_2[0]["interval"]:
        interval_1[0]["interval"].append(value)  # 前部分填充

    for i in range(3):
        interval_1[1][i] += interval_2[1][i]  # 后部分相加

    return interval_1


def chiMerge(attribute_list, max_interval=6):
    num_interval = len(attribute_list)

    while (num_interval > max_interval):
        chi2_list = []
        for i in range(len(attribute_list) - 1):
            chi2_value = chi2(attribute_list[i][1], attribute_list[i + 1][1])
            chi2_list.append(chi2_value)
        # print("chi2_list", chi2_list)
        min_chi2 = min(chi2_list)  # 求最小的卡方值
        # print("min_chi2:", min_chi2)
        min_index = chi2_list.index(min_chi2)
        attribute_list[min_index] = merge(attribute_list[min_index], attribute_list[min_index + 1])  # 合并
        del attribute_list[min_index + 1]

        num_interval = len(attribute_list)

    return attribute_list


def perform_data_discretization(iris_list, attribute_num):
    sepal_lengthList = initial_interval(iris_list, attribute_num)  # 初始化属性区间列表，这里以iris的第一个属性sepal_length为例
    result = chiMerge(sepal_lengthList)  # 进行ChiMerge离散化
    # print(result)
    # 打印相应信息
    for i in range(len(result)):
        if attribute_num == 0:
            print("\n第" + str(i + 1) + "个sepal_length属性区间的值为：\n", result[i][0]["interval"])
        elif attribute_num == 1:
            print("\n第" + str(i + 1) + "个sepal_width属性区间的值为：\n", result[i][0]["interval"])
        elif attribute_num == 2:
            print("\n第" + str(i + 1) + "个petal_length属性区间的值为：\n", result[i][0]["interval"])
        elif attribute_num == 3:
            print("\n第" + str(i + 1) + "个petal_width属性区间的值为：\n", result[i][0]["interval"])
        else:
            return
        print("\n该区间所对应的类别信息为：")
        print("Iris-setosa: ", '*' * result[i][1][0], "  共", result[i][1][0], "个",
              "\nIris-versicolor: ", '*' * result[i][1][1], "  共", result[i][1][1], "个",
              "\nIris-virginica: ", '*' * result[i][1][2], "  共", result[i][1][2], "个")


def main():
    iris_list = read_data(filename)  # 读取数据
    for i in range(4):
        perform_data_discretization(iris_list, i)


if __name__ == '__main__':
    main()
