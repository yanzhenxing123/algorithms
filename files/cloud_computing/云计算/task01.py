"""
@Author: yanzx
@Date: 2021-11-14 18:37:27
@Desc: 
"""
from pyspark import SparkContext
import os
import pandas as pd

os.environ['JAVA_HOME'] = '/Library/Java/JavaVirtualMachines/jdk1.8.0_301.jdk/Contents/Home'  # 这里的路径为java的bin目录所在路径


def get_taxi_numbers_func1():
    """
    使用Series对象去重
    :return:
    """
    df = pd.read_csv("data/taxi_gps.txt", header=None)
    df_id = df[0]
    print("使用Series对象去重获得taxi的数量：" + str(len(df_id.unique())))


def get_taxi_numbers_func2():
    """
    使用set集合进行去重
    :return:
    """
    taxi_ids = set()
    with open("data/taxi_gps.txt", "r", encoding="utf-8") as fp:
        for line in fp:
            taxi_id = line.split(",")[0]
            taxi_ids.add(taxi_id)
    print("使用set集合进行去重获得taxi的数量：" + str(len(taxi_ids)))


def get_taxi_numbers_func3():
    """
    使用spark RDD distinct进行去重
    :return:
    """
    sc = SparkContext('local', 'taxi_count')
    rdd = sc.textFile("./data/taxi_gps.txt")

    flat_rdd = rdd.flatMap(lambda x: x.split(",")[0:1])
    taxi_distinct = flat_rdd.distinct()
    print("使用flatmap后对RDD去重获得taxi的数量：", len(taxi_distinct.collect()))
    counts = taxi_distinct.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
    print("去重后使用wordcount获得taxi的数量：", counts.count())


if __name__ == '__main__':
    get_taxi_numbers_func1()
    get_taxi_numbers_func2()
    get_taxi_numbers_func3()
