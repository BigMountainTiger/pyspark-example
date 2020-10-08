from pyspark import SparkContext, SparkConf
import os

def getAListFromAFile(file_path):
  lines = open(file_path).read().splitlines()
  lines.append('From process ({})'.format(os.getpid()))

  return lines

def run():
  conf = SparkConf().setAppName("word count") \
    .setMaster("local[2]")

  context = SparkContext(conf = conf)
  context.setLogLevel('ERROR')
  
  dir = '/home/song/Sandbox/pyspark-example/files/{}'
  path_1 = dir.format('file-1.txt')
  path_2 = dir.format('file-2.txt')

  file_paths = [path_1, path_2]
  rdd = context.parallelize(file_paths, 2) \
    .flatMap(getAListFromAFile).cache()
  
  print('No of partitions = {}'.format(rdd.getNumPartitions()))
  wordCounts = rdd.countByValue()
  for word, count in wordCounts.items():
      print("{} : {}".format(word, count))

  count = rdd.count()
  print('Total count = {}'.format(count))

if __name__ == "__main__":
  run()