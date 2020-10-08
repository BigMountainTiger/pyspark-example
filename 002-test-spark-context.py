import sys
from pprint import pprint
from pyspark import SparkContext, SparkConf

def run():
  print(sys.argv)
  conf = SparkConf()
  conf.setAppName("Test App Name")

  # spark-submit --master local[3] 002-test-spark-context.py
  # This override the spark-submit "--master" parameter
  conf.setMaster('local[2]')

  context = SparkContext(conf = conf)
  pprint(vars(context))
  

if __name__ == "__main__":
  run()