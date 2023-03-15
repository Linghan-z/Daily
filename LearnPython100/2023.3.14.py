# -*- coding: utf-8 -*-
# @File : 2023.3.14.py
# @Time : 3/14/23 16:50

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# 判断素数
from math import sqrt


def is_prime(x):
    isPrime = True
    x_sqrt = int(sqrt(x))
    for i in range(2, x_sqrt):
        if x % i == 0:
            isPrime = False
    return isPrime


# 百钱百🐔

def money_and_chicken():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if (5 * x + 3 * y + z / 3) == 100:
                print("%d🐓 ，%d🐔， %d🐤" % (x, y, z))


# 斐波那契数列
def fibonacci_sequence(num1, num2):
    if num2 == 1:
        print(1)
        print(1)
    num3 = num1 + num2
    print(num3)
    if num3 < 100:
        fibonacci_sequence(num2, num3)


if __name__ == '__main__':
    # x = int(input("请输入一个数字："))
    # print(is_prime(x))
    # money_and_chicken()
    fibonacci_sequence(1, 1)
