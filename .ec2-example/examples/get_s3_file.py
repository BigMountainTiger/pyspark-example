import boto3
import socket
from pyspark.sql import SparkSession

def get_hostname():
    return socket.gethostname()

def get_s3_file(NAME):
    s3 = boto3.resource('s3')
    BUCKET = 'example.huge.head.li'

    content = s3.Object(BUCKET, NAME).get()['Body'].read().decode(
        'utf-8').splitlines()

    return f'{content[0]} from {get_hostname()}'


def run():
    NAME = 'GET_S3_FILES'
    PARTITIONS = 2

    spark = SparkSession.builder.appName(NAME).getOrCreate()
    rdd = spark.sparkContext.parallelize(
        ['text-1', 'text-2'], PARTITIONS).map(get_s3_file)

    for text in rdd.collect():
        print(text)

    spark.stop()


if __name__ == '__main__':
    run()

# This is to demonstrate that spark slaves can read S3 files independently
# This requires to put two files on the S3, they will be read in parallel