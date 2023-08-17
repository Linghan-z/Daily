#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File    : neo4j_node_id.py
# @Time    : 6/18/23 11:04
# @Author  : zlhhh
# @Description :


import mysql.connector
from neo4j import GraphDatabase

# 连接到MySQL数据库
mysql_conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="19991125",
    database="network_security"
)
mysql_cursor = mysql_conn.cursor()

# 从MySQL数据库查询数据
mysql_cursor.execute("SELECT id, value FROM neo4j_node_entity")
mysql_data = mysql_cursor.fetchall()

# 连接到Neo4j数据库
neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "123456")
)

# 从Neo4j数据库查询ID
neo4j_session = neo4j_driver.session()
neo4j_data = []
for mysql_row in mysql_data:
    neo4j_result = neo4j_session.run(
        "MATCH (n {value: $value}) RETURN id(n)",
        value=mysql_row[1]
    )
    neo4j_row = neo4j_result.single()
    if neo4j_row is not None:
        neo4j_data.append((neo4j_row[0], mysql_row[0]))

# 使用Neo4j ID更新MySQL数据库
mysql_cursor.executemany(
    "UPDATE neo4j_node_entity SET neo4j_id = %s WHERE id = %s",
    neo4j_data
)
mysql_conn.commit()

# 关闭数据库连接
neo4j_session.close()
neo4j_driver.close()
mysql_cursor.close()
mysql_conn.close()