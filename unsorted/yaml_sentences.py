#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : yaml_sentences.py
# @Time    : 8/12/23 12:44
# @Author  : zlhhh
# @Description :

import csv


def generate_organization_sentences(filename):
    sentences = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过标题行
        for row in reader:
            entity = row[0]
            sentence = [
                f"      - [{entity}](organization)的[简介](attribute)",
                f"      - [{entity}](organization)的[出现时间](attribute)",
                f"      - [{entity}](organization)的[目的](attribute)",
                f"      - [{entity}](organization)是[什么](attribute)",
                f"      - [{entity}](organization)的[链接](attribute)",
                f"      - [什么](attribute)是[{entity}](organization)",
            ]
            sentences.extend(sentence)

    return sentences


def generate_attacktype_sentences(filename):
    sentences = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过标题行
        for row in reader:
            entity = row[0]
            sentence = [
                f"      - [{entity}](attacktype)的简介",
                f"      - [{entity}](attacktype)是什么",
                f"      - [{entity}](attacktype)的意思",
                f"      - [{entity}](attacktype)的内容",
                f"      - [{entity}](attacktype)的介绍",
                f"      - 什么是[{entity}](attacktype)",
            ]
            sentences.extend(sentence)

    return sentences


def generate_domain_sentences(filename):
    sentences = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过标题行
        for row in reader:
            entity = row[0]
            sentence = [
                f"      - [{entity}](domain)是什么",
                f"      - [{entity}](domain)的值",
                f"      - [{entity}](domain)的域名",
                f"      - [{entity}](domain)的网址",
                f"      - [{entity}](domain)指什么",
                f"      - 什么是[{entity}](domain)",
            ]
            sentences.extend(sentence)

    return sentences


def generate_ip_sentences(filename):
    sentences = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过标题行
        for row in reader:
            entity = row[0]
            sentence = [
                f"      - [{entity}](ip)是什么",
                f"      - [{entity}](ip)的值",
                f"      - [{entity}](ip)的ip",
                f"      - [{entity}](ip)的地址",
                f"      - [{entity}](ip)指什么",
                f"      - 什么是[{entity}](ip)",
            ]
            sentences.extend(sentence)

    return sentences


def generate_sha256_sentences(filename):
    sentences = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # 跳过标题行
        for row in reader:
            entity = row[0]
            sentence = [
                f"      - [{entity}](organization)攻击了哪些行业",
                f"      - [{entity}](organization)针对哪些行业",
                f"      - [{entity}](organization)主要攻击哪些行业",
                f"      - 哪些行业被[{entity}](organization)攻击",
                f"      - 给我列举一些[{entity}](organization)攻击的行业",
            ]
            sentences.extend(sentence)

    return sentences


def generate_industry_sentences(filename):
    sentences = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            entity = row[0]
            sentence = [
                f"      - 哪些组织攻击了[{entity}](industry)",
                f"      - 有哪些组织攻击[{entity}](industry)业",
                f"      - [{entity}](industry)被哪些组织攻击",
                f"      - [{entity}](industry)被哪些组织攻击过",
                f"      - 给我列举一些攻击[{entity}](industry)的组织",
            ]
            sentences.extend(sentence)

    return sentences


def generate_industry_sentences_reversed(filename):
    sentences = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            entity = row[0]
            sentence = [
                f"      - [{entity}](organization)攻击了哪些行业",
                f"      - [{entity}](organization)针对哪些行业",
                f"      - [{entity}](organization)主要攻击哪些行业",
                f"      - 哪些行业被[{entity}](organization)攻击",
                f"      - 给我列举一些[{entity}](organization)攻击的行业",
            ]
            sentences.extend(sentence)

    return sentences

#
# filename = '../neo4j/data/ctiic/vertex_organization.csv'
# sentences = generate_organization_sentences(filename)
#
# # 将生成的句子输出到txt文件
# with open('../neo4j/data/ctiic/yaml/organization.txt', 'w', encoding='utf-8') as file:
#     for sentence in sentences:
#         file.write(sentence + '\n')
#
# filename = '../neo4j/data/ctiic/vertex_attacktype.csv'
# sentences = generate_attacktype_sentences(filename)
#
# # 将生成的句子输出到txt文件
# with open('../neo4j/data/ctiic/yaml/attacktype.txt', 'w', encoding='utf-8') as file:
#     for sentence in sentences:
#         file.write(sentence + '\n')
#
# filename = '../neo4j/data/ctiic/vertex_domain.csv'
# sentences = generate_domain_sentences(filename)
#
# # 将生成的句子输出到txt文件
# with open('../neo4j/data/ctiic/yaml/domain.txt', 'w', encoding='utf-8') as file:
#     for sentence in sentences:
#         file.write(sentence + '\n')
#
# filename = '../neo4j/data/ctiic/vertex_ip.csv'
# sentences = generate_ip_sentences(filename)
#
# # 将生成的句子输出到txt文件
# with open('../neo4j/data/ctiic/yaml/ip.txt', 'w', encoding='utf-8') as file:
#     for sentence in sentences:
#         file.write(sentence + '\n')
#
# filename = '../neo4j/data/ctiic/vertex_sha256.csv'
# sentences = generate_sha256_sentences(filename)
#
# # 将生成的句子输出到txt文件
# with open('../neo4j/data/ctiic/yaml/sha256.txt', 'w', encoding='utf-8') as file:
#     for sentence in sentences:
#         file.write(sentence + '\n')

# filename = '../neo4j/data/ctiic/vertex_industry.csv'
# sentences = generate_industry_sentences(filename)
#
# # 将生成的句子输出到txt文件
# with open('../neo4j/data/ctiic/yaml/industry.txt', 'w', encoding='utf-8') as file:
#     for sentence in sentences:
#         file.write(sentence + '\n')
filename = '../neo4j/data/ctiic/vertex_organization.csv'
sentences = generate_industry_sentences_reversed(filename)

# 将生成的句子输出到txt文件
with open('../neo4j/data/ctiic/yaml/industry_reversed.txt', 'w', encoding='utf-8') as file:
    for sentence in sentences:
        file.write(sentence + '\n')

