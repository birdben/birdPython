#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
from elasticsearch import Elasticsearch

todayDate = datetime.date.today()
yesterdayDate = todayDate - datetime.timedelta(days=1)

todayFormatDate = todayDate.strftime('%Y.%m.%d')
yesterdayFormatDate = yesterdayDate.strftime('%Y.%m.%d')

print(todayFormatDate)
print(yesterdayFormatDate)

# 第三方 SMTP 服务
# SMTP 服务器
mail_host = "smtpdm.aliyun.com"
# SMTP 用户名
mail_user = "service@post.XXX.com"
# SMTP 密码
mail_pass = "123456"
# SMTP 端口号
mail_port = 25

sender = 'service@post.XXX.com'
# 接收邮件，可设置为你的QQ邮箱或者其他邮箱
receivers = ['birdben@XXX.com']

mail_body_start = "<p>" + yesterdayFormatDate + " Go Access慢请求日志</p>"
mail_body_content = ""
mail_body_end = "<p>此邮件由系统自动发送</p>"

# 索引名称：go_access_logs_index_2017.02.16
es_host = "localhost"
es_port = "9200"
es_query_index = "go_access_logs_index_" + yesterdayFormatDate
# es_query_api = "/_cat/indices"
es_query_api = "/_search"
es_query_body = {
    "query": {"filtered": {"filter": {"bool": {"must": [{"range": {"request_time": {"lte": 5, "gte": 3}}}]}}}},
    "fields": ["request_id", "url", "request_time", "timestamp"], "size": 100, "sort": [{"request_time": "desc"}]}

es_query_baseUrl = "/" + es_query_index + es_query_api

try:
    print("es_query_baseUrl:" + es_query_baseUrl)
    es = Elasticsearch([{
        'host': es_host,
        'port': es_port
    }])
    headers = {'Content-type': 'application/json'}

    returnObj = es.search(
        index=es_query_index,
        doc_type=None,
        scroll=None,
        search_type=None,
        size=None,
        body=es_query_body
    )

    # 不能这么输出，否则会报错
    # print("returnObj:" + returnObj)
    print(returnObj)
    total = returnObj['hits']['total']
    print(total)
    if total > 0:
        returnObjList = returnObj['hits']['hits']
        # 创建迭代器对象
        it = iter(returnObjList)
        #f = open('go_access_slow_response.txt', 'a+')
        for x in it:
            #print(str(x['fields']))
            row_request_id = ""
            row_url = ""
            row_request_time = ""
            row_timestamp = ""

            fields = x['fields']
            if 'request_id' in fields.keys():
                row_request_id = str(x['fields']['request_id'])
                print("row_request_id:" + row_request_id)
            if 'url' in fields.keys():
                row_url = str(x['fields']['url'])
                print("row_url:" + row_url)
            if 'request_time' in fields.keys():
                row_request_time = str(x['fields']['request_time'])
                print("row_request_time:" + row_request_time)
            if 'timestamp' in fields.keys():
                row_timestamp = str(x['fields']['timestamp'])
                print("row_timestamp:" + row_timestamp)
            #f.write(row_request_id + row_url + row_request_time + row_timestamp + '\n')
            #f.flush()
            mail_body_content = mail_body_content + (row_request_id + row_url + row_request_time + row_timestamp + "<br>")
        #f.close()
except:
    print('got error when request URL ' + es_query_baseUrl + '\n')

mail_content = mail_body_start + mail_body_content + mail_body_end

message = MIMEText(mail_content, 'html', 'utf-8')
message['From'] = Header("service", 'utf-8')
message['To'] = Header("服务端组", 'utf-8')

subject = yesterdayFormatDate + ' Go Access慢请求日志'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, mail_port)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")
