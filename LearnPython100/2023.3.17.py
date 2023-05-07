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


def dic_en_zh():
    military_attributes_in_en = ['name', 'origin_country', 'img_url', 'introduction', 'first_fly_time',
                                 'R&D_organization',
                                 'pneumatic_layout', 'num_of_engine', 'speed', 'attention_degree', 'crew_num',
                                 'flight_long', 'wings_width', 'flight_height', 'engine', 'max_speed', 'max_voyage',
                                 'class', 'categories', 'serve_time', 'producer', 'net_weight', 'max_fly_weight',
                                 'retire_time', 'rotor_diameter', 'machine_gun', 'mount_point', 'built-in_weapon',
                                 'war_field_machine_type', 'W-3W', 'build_time', 'full_tonnage_row', 'authorized',
                                 'captain', 'modeled_breath', 'load_displacement', 'cruising_distance',
                                 'navigational_speed', 'manufactory', 'launch_time', 'status', 'same_type',
                                 'activity_range', 'prior_type', 'latter_type', 'self-sustaining', 'missile',
                                 'cannon', 'modify_time', 'water_displacement', 'firing_control_device', 'main_cannon',
                                 'submersible_depth', 'before_modify', 'complete_time', 'equipment', 'Armed',
                                 'military_uniform', '1935', 'anti-ship_missile', 'ship-to-ship_missile',
                                 'new_build', 'anti-aircraft-weapon', 'under_water_displacement', 'weapon_equipment',
                                 'torpedo', 'mine', 'arms', 'shooter', 'firearms', 'manufacturer', 'produce_year',
                                 'amount', 'calibres',
                                 'gun_length', 'gun_weight', 'magazine_capacity',
                                 'war_participation', 'effective_range', 'shoot_performance', 'shoot_speed',
                                 'knife_length', 'blade_length', 'blade_width', 'knife_weight', 'R&D_manufactures',
                                 'born_time', 'chassis_type', 'crew_num', 'vehicle_length', 'width', 'height',
                                 'weight_in_war', 'max_speed', 'max_route', 'gross_weight', 'barrel_length',
                                 'max_range', 'muzzle_velocity', 'R&D_time', 'editor_rating', 'version', 'tital_length',
                                 'development_time', 'shoot_range', 'bullet_length',
                                 'bullet_diameter',
                                 'bullet_weight', 'guidance_sys', 'fuze', 'launch_date', 'launch_place', 'length',
                                 'center_diameter', 'first_orbital_launch', 'orbit', 'longitude', 'latitude',
                                 'carrier_rocket', 'processor', 'orbiting_satellites', 'charge_type', 'total_weight',
                                 'fuze_device', 'tail_device', 'power_device']
    military_attributes = ['名称', '产国', '图片', '简介', '首飞时间', '研发单位', '气动布局', '发动机数量', '飞行速度',
                           '关注度', '乘员',
                           '机长', '翼展', '机高', '发动机', '最大飞行速度', '最大航程', '大类', '类型', '服役时间',
                           '生产单位',
                           '空重',
                           '最大起飞重量', '退役时间', '旋翼直径', '机炮', '挂载点', '内置武器', '战地机型', 'W-3W',
                           '建造时间',
                           '满排吨位', '编制',
                           '舰长', '型宽', '满载排水量', '续航距离', '航速', '制造厂', '下水时间', '现状', '同型',
                           '活动范围',
                           '前型', '次型',
                           '自持力', '导弹', '火炮', '改装时', '水上排水量', '射控装置', '主炮', '潜航深度', '改装前',
                           '竣工时',
                           '装备', '武备',
                           '兵装', '1935年', '反舰导弹', '舰舰导弹', '新造时', '防空兵器', '水下排水量', '武器装备',
                           '鱼雷',
                           '水雷', '武装',
                           '枪械', '枪炮', '制造商', '生产年限', '数量', '口径', '全枪长', '全枪重', '弹匣容弹量',
                           '参战情况',
                           '有效射程', '发射性能',
                           '战斗射速', '刀长', '刀锋长度', '刀锋宽度', '刀重', '研发厂商', '诞生时间', '底盘类型',
                           '乘员与载员',
                           '车长', '宽度',
                           '高度', '战斗全重', '最大速度', '最大行程', '总重', '炮管长度', '最大射程', '炮口初速',
                           '研发时间',
                           '编辑评分', '型号',
                           '全长', '研制时间', '射程', '弹长', '弹径', '弹重', '制导系统', '引信', '发射日期',
                           '发射地点', '长度',
                           '中心直径',
                           '首次轨道发射', '轨道', '纬度', '经度', '运载火箭', '处理器', '轨道卫星', '装药类型', '全重',
                           '引信装置', '尾翼装置',
                           '动力装置']
    dic = {}
    f = open('./dic.json', 'a', encoding='utf-8')
    for i in range(len(military_attributes)):
        dic[military_attributes_in_en[i]] = military_attributes[i]
    for i in range(len(military_attributes)):
        print(dic)


def main():
    dic_en_zh()


if __name__ == '__main__':
    main()
