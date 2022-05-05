import socket
from pyspark.sql import SparkSession


def get_hostname(i):
    return socket.gethostname()


def run():
    NAME = 'GET_HOST_NAME'
    PARTITIONS = 2

    spark = SparkSession.builder.appName(NAME).getOrCreate()
    rdd = spark.sparkContext.parallelize(
        range(0, 2), PARTITIONS).map(get_hostname)

    for ip in rdd.collect():
        print(ip)

    spark.stop()


if __name__ == '__main__':
    run()
