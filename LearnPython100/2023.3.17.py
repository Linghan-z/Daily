# -*- coding: utf-8 -*-
# @File : 2023.3.17.py
# @Time : 3/17/23 12:49
import sys
from math import sqrt


# 完美数
def factorize(k):
    factors = []
    sum = 0
    for i in range(1, k):
        if k % i == 0:
            factors.append(i)

    for num in factors:
        sum += num
    if sum == k:
        print(k)


def str_test():
    str2 = 'abc123456'
    str1 = '1212121'
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50, '*'))
    print(str2[-3:-1])


def list_test():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a
        print("continue....")


def set_test():
    # 创建集合的字面量语法
    set1 = {1, 2, 3, 3, 3, 2}
    # 创建集合的构造器语法(面向对象部分会进行详细讲解)
    set2 = set(range(1, 10))
    print(set2)
    set3 = set((1, 2, 3, 3, 2, 1))
    # 创建集合的推导式语法(推导式也可以用于推导集合)
    set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
    set1.add(4)
    set1.add(5)
    set2.update([11, 12])
    set2.discard(5)
    if 4 in set2:
        set2.remove(4)
    print(set1, set2)
    print(set3.pop())
    print(set3)


def dict_test():
    # 创建字典的字面量语法
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    print(scores)
    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)
    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))
    # 创建字典的推导式语法
    items3 = {num: num ** 2 for num in range(1, 10)}
    print(items1, items2, items3)
    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 对字典中所有键值对进行遍历
    for key in scores:
        print(f'{key}: {scores[key]}')
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('a', 100))
    # 清空字典
    print(scores)
    scores.clear()
    print(scores)


import os
import time


# 跑马灯文字
def text_run():
    context = 'ZZZZZLLLLLHHHHH'
    while True:
        os.system('clear')
        print(context)
        time.sleep(0.2)
        content = content[1:] + content[0]


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    filename_suffix = filename.split('.')[-1]
    print(filename_suffix)
    print('#' * 20)
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def max2(num_list):
    sorted_num_list = sorted(num_list, reverse=True)
    for i in range(0, 2):
        print(sorted_num_list[i])


class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    print('Good Night')
                    self.hour = 0

    def show(self):
        return '%02d:%02d:%02d' % \
            (self.hour, self.minute, self.second)


from time import sleep


# def main():
#     clock = Clock(23, 58, 40)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()


class Person(object):
    __slots__ = {'_name', '_age', 'eat', 'play'}

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name


class Student(Person):
    __slots__ = {'study', '_grade'}

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade


class Teacher(Person):
    __slots__ = {'_title', '_teach'}

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title


def aa():
    num1 = ['1', '2', '3', '4', '5']
    num2 = '12345'

    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    print(list(map(char2num, num1)))
    print(list(map(char2num, num2)))


def main():
    aa()


if __name__ == '__main__':
    main()
