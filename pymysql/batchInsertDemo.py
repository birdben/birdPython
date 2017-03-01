#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root", password="root", db="test", charset="utf8mb4")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()

# 输出MySQL的版本信息
# print("Database version : %s " % data)

start_user_id = 2

start_st_user_id = 10000

sql = "SELECT ID, NAME FROM USER WHERE ID > %d"

try:
    # 执行sql语句
    cursor.execute(sql % (start_user_id))
    # 获取所有记录列表
    results = cursor.fetchall()
except Exception as e:
    print(e)

# SQL 插入语句
st_user_sql = """INSERT INTO ST_USER (ST_USER_ID, COMPANY_ID, REF_USER_ID, REF_USER_NAME, CREATED_DT, MODIFIED_DT)
    values ('%d', '%s', '%d', '%s', now(), now());"""

i = 0

for result in results:
    i += 1
    print(result[0])
    print(result[1])

    st_user_id = start_st_user_id + i
    company_id = "999999999"
    ref_user_id = result[0]
    ref_user_name = result[1]

    try:
        # 执行sql语句
        cursor.execute(st_user_sql % (st_user_id, company_id, ref_user_id, ref_user_name))
        # 提交到数据库执行
        db.commit()
        print("插入成功")

    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
        print(e)

# 关闭数据库连接
db.close()
