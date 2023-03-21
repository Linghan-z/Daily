#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : entity_from_json.py
# @Time    : 3/20/23 20:33
# @Author  : zlhhh
# @Description : 从 military.json 中获取实体

import json


def read_json(str):
    data_path = './data/military.json'
    entity = []
    for data in open(data_path, encoding='utf8'):
        data_json = json.loads(data)
        if str in data_json:
            entity.append(data_json[str]+ '\n')
    return set(entity)


def write_txt(data_path, data_list):
    f = open(data_path, 'a', encoding='utf-8')
    f.writelines(data_list)
    f.close()


def read_and_write(data_path, name):
    entity_list = read_json(name)
    write_txt(data_path, entity_list)


def main():
    # node_attributes = ['产国', '研发单位', '研发厂商', '大类', '类型', '制造商', '制造厂',
    #                    '活动范围', '底盘类型', '口径', '型号', '气动布局']
    read_and_write('./data/military.txt', '名称')
    read_and_write('./data/country.txt', '产国')
    read_and_write('./data/R&Q_organization.txt', '研发单位')
    read_and_write('./data/R&Q_organization.txt', '研发厂商')
    read_and_write('./data/class.txt', '大类')
    read_and_write('./data/category.txt', '类型')
    read_and_write('./data/producer.txt', '制造商')
    read_and_write('./data/producer.txt', '制造厂')
    read_and_write('./data/activity_area.txt', '活动范围')
    read_and_write('./data/armored_car_chassis_types.txt', '底盘类型')
    read_and_write('./data/cannon_calibres.txt', '口径')
    read_and_write('./data/cannon_types.txt', '型号')
    read_and_write('./data/pneumatic_layout.txt', '气动布局')


if __name__ == '__main__':
    main()
