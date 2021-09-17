"""
@Author: yanzx
@Date: 2021-09-16 00:10:03
@Desc: 
"""
import json

from db import MysqlConn, Consumer
from config import Kafka

def get_data():
    kafka = Consumer(Kafka['Topics'])
    for msg in kafka.confluent_consumer(timeout=1.00):
        yield msg
        break

def main():
    for data in get_data():
        print(data.topic())
        res = str(data.value(), encoding='utf8')
        print(res)
        print(res.split())
        break


if __name__ == '__main__':
    # conn = MysqlConn.get_conn()
    # cursor = conn.cursor()
    # res = cursor.execute("show tables")

    main()