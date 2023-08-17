#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : delete_quotes_in_yaml.py
# @Time    : 8/12/23 13:24
# @Author  : zlhhh
# @Description :

import yaml

# 读取 YAML 文件
with open('../neo4j/data/ctiic/yaml/output.yml', 'r') as file:
    data = yaml.safe_load(file)

# 删除引号
def remove_quotes(value):
    if isinstance(value, str):
        return value.replace("'", "").replace('"', "")
    elif isinstance(value, list):
        return [remove_quotes(item) for item in value]
    elif isinstance(value, dict):
        return {remove_quotes(key): remove_quotes(val) for key, val in value.items()}
    return value

# 删除引号后的数据
data_without_quotes = remove_quotes(data)

# 将更新后的数据写入新的 YAML 文件
with open('../neo4j/data/ctiic/yaml/nlu.yml', 'w') as file:
    yaml.safe_dump(data_without_quotes, file, allow_unicode=True, default_style='', default_flow_style=False)