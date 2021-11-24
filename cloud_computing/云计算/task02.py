# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from socket import socket

import findspark
import os
from pyspark import SparkConf, SparkContext
from math import radians, cos, sin, asin, sqrt

os.environ['JAVA_HOME'] = '/Library/Java/JavaVirtualMachines/jdk1.8.0_301.jdk/Contents/Home'  # 这里的路径为java的bin目录所在路径

findspark.init()


def haversine(taxi, district):
    """
    两个坐标经纬度获取距离
    :param taxi: 出租车坐标
    :param district: 地区中心坐标
    :return:
    """
    # 将十进制度数转化为弧度
    t_lon, t_lat, d_lon, d_lat = map(
        radians,
        map(float, [taxi[0], taxi[1], district[0], district[1]])  # 转化为float
    )
    # haversine公式
    dlon = d_lon - t_lon
    dlat = d_lat - t_lat
    a = sin(dlat / 2) ** 2 + cos(t_lat) * cos(d_lat) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371.393  # 地球平均半径，单位为公里
    return c * r


def get_label(distance, r):
    """
    给每一个车辆进行打标
    :return:
    """
    return 1 if distance <= r else 0


def main():
    """
    主函数
    """
    conf = SparkConf().setMaster("local[*]").setAppName("First_App")
    sc = SparkContext(conf=conf)
    # 读取数据集
    district = sc.textFile(u'./data/district.txt')
    taxi_gps = sc.textFile(u'./data/taxi_gps.txt')
    # 只取数据集中的经纬度
    district_data = district.map(lambda line: line.split(','))
    taxi_data = taxi_gps.map(lambda line: line.split(',')[4:6])
    # 对两个数据集进行笛卡尔积操作
    merge_data = taxi_data.cartesian(district_data)
    # merge_data.foreach(print)
    # 对数据集进行打标
    taxi_label = merge_data.map(lambda a: (a[1][0], get_label(haversine(a[0], a[1][1:3]), float(a[1][3]))))
    cnt = taxi_label.filter(lambda x: x[1] == 1).reduceByKey(lambda x, y: x + y)
    for i in cnt.collect():
        print(i[0] + "点数为: ", i[1])


if __name__ == '__main__':
    main()
