"""
@Author: yanzx
@Date: 2021-09-16 00:48:26
@Desc: 
"""
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

def start():
    conf = SparkConf().set("spark.python.profile", "true").\
        set("spark.io.compression.codec", "snappy") #.setMaster('local[*]')
    conf.setAppName('spark-test')
    sc = SparkContext(conf=conf)
    ssc=StreamingContext(sc,6)

    brokers="xxx:6667,xxx:6667,xxx:666"
    topic='streamtopic'
    kafkaStreams = KafkaUtils.createDirectStream(ssc,[topic],kafkaParams={"metadata.broker.list": brokers})
    result=kafkaStreams.map(lambda x:(x[1],1)).reduceByKey(lambda x, y: x + y)
    kafkaStreams.transform(storeOffsetRanges).foreachRDD(printOffsetRanges)
    result.pprint()
    ssc.start()
    ssc.awaitTermination()

offsetRanges = []

def storeOffsetRanges(rdd):
    global offsetRanges
    offsetRanges = rdd.offsetRanges()
    return rdd

def printOffsetRanges(rdd):
    for o in offsetRanges:
        print("%s %s %s %s %s" % (o.topic, o.partition, o.fromOffset, o.untilOffset,o.untilOffset-o.fromOffset))

if __name__ == '__main__':
    start()
