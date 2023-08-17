#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : ImportIntoMysql.py
# @Time    : 6/6/23 13:30
# @Author  : zlhhh
# @Description :

import csv
import mysql.connector

# MySQL数据库连接信息
db_config = {
    'user': 'root',
    'password': '19991125',
    'host': 'localhost',
    'port': 3306,
    'database': 'network_security',
    'auth_plugin': 'caching_sha2_password'
}


def import_node_data(filepath, connection, start_column, *args):
    with open(filepath, 'r') as csv_file:
        # 创建csv.reader对象
        csv_reader = csv.reader(csv_file)
        # 获取MySQL游标
        cursor = connection.cursor()

        # 遍历CSV文件中的每一行
        for row in csv_reader:
            # 忽略标题行
            if csv_reader.line_num == 1:
                continue

            attributes = ', '.join(args)
            values_placeholder = ', '.join(['%s'] * len(args))
            values = tuple(row[start_column:start_column + len(args)])

            print("++++++++++++++" + attributes)
            print("++++++++++++++" + values_placeholder)
            print(values)

            # 执行INSERT语句
            insert_query = "INSERT INTO neo4j_node_entity ({}) VALUES ({})".format(attributes, values_placeholder)
            cursor.execute(insert_query, values)
        # 提交更改
        connection.commit()


def node_data(connection):
    import_node_data('./data/ctiic/vertex_organization.csv', connection, 0, "value", "occurtime", "motivation",
                     "introduction", "referlink")
    import_node_data('./data/ctiic/vertex_area.csv', connection, 0, "value")
    import_node_data('./data/ctiic/vertex_industry.csv', connection, 0, "value")
    import_node_data('./data/ctiic/vertex_attacktype.csv', connection, 0, "value", "introduction")
    import_node_data('./data/ctiic/vertex_ip.csv', connection, 0, "link_identifier", "value")
    import_node_data('./data/ctiic/vertex_domain.csv', connection, 0, "link_identifier", "value")
    import_node_data('./data/ctiic/vertex_sha256.csv', connection, 0, "link_identifier", "value", "format")


def import_triples_data(filepath, connection, rel, query_field='link_identifier'):
    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        cursor = connection.cursor()
        for row in csv_reader:
            # 忽略标题行
            if csv_reader.line_num == 1:
                continue
            query = """
            INSERT INTO neo4j_triples (head_id, head_value, head_label, relation, tail_id, tail_value, tail_label)
            SELECT
                entity.id         AS head_id,
                entity.value      AS head_value,
                entity.label      AS head_label,
                %s                AS relation,
                tail_entity.id    AS tail_id,
                tail_entity.value AS tail_value,
                tail_entity.label AS tail_label
            FROM
                neo4j_node_entity entity
                INNER JOIN neo4j_node_entity tail_entity ON tail_entity.{} = %s 
            WHERE
                entity.label = 'organization'
                AND entity.value = %s;""".format(query_field)
            values = (rel, row[1], row[0])
            cursor.execute(query, values)
            # result = cursor.fetchall()
            # print(result)
        connection.commit()

def triple_data(connection):
    import_triples_data('./data/ctiic/edge_organization_from.csv',connection,"edge_organization_from","value")
    import_triples_data('./data/ctiic/edge_organization_has_area.csv',connection,"edge_organization_has_area","value")
    import_triples_data('./data/ctiic/edge_organization_has_attacktype.csv',connection,"edge_organization_has_attacktype","value")
    import_triples_data('./data/ctiic/edge_organization_has_industry.csv',connection,"edge_organization_has_industry","value")
    import_triples_data('./data/ctiic/edge_organization_has_ip.csv',connection,"edge_organization_has_ip")
    import_triples_data('./data/ctiic/edge_organization_has_domain.csv',connection,"edge_organization_has_domain")
    import_triples_data('./data/ctiic/edge_organization_has_sha256.csv',connection,"edge_organization_has_sha256")

def main():
    try:
        connection = mysql.connector.connect(**db_config)
        print("Connection established")
        triple_data(connection)
        # node_data(connection)
        # 关闭MySQL连接
        connection.close()
    except mysql.connector.Error as error:
        print("Error: {}".format(error))


if __name__ == '__main__':
    main()
    # print(1)
