#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : 2023.5.07.py
# @Time    : 5/7/23 21:00
# @Author  : zlhhh
# @Description :
import numpy as np


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


def main():
    x = [1.4, 1.6]
    # x1 = [1.5, 1.7]
    # x2 = [2, 1.9]
    # x3 = [1.6, 1.8]
    # x4 = [1.2, 1.5]
    # x5 = [1.5, 1.0]
    y = [[1.5, 1.7], [2, 1.9], [1.6, 1.8], [1.2, 1.5], [1.5, 1.0]]
    z = []
    for item in y:
        # calculation(x, item)

        z.append(norm(item))
    # print(z)
    x_norm = norm(x)
    print(x_norm)
    for item in z:
        print(euclidean_distance(x_norm, item))


if __name__ == '__main__':
    main()
