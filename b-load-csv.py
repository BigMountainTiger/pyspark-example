
import sys
import os
import socket
import pyspark
import pyspark.sql.functions as F
from pyspark import SparkContext, SQLContext, SparkConf
from pyspark.sql import Row

def newValue():
  #return 'From process ({}) - ({})'.format(os.getpid(), socket.gethostname())
  return '({})'.format(socket.gethostname())


def run():

  print(pyspark.__file__)

  # Get the module search path
  for p in sys.path:
    print(p)

  conf = SparkConf().setAppName('load CSV')

  context = SparkContext(conf = conf)
  context.setLogLevel('ERROR')
  sqlContext = SQLContext(context)

  df_name = sqlContext.read.csv('/home/song/Sandbox/pyspark-example/files/name.csv', header=True)
  df_score = sqlContext.read.csv('/home/song/Sandbox/pyspark-example/files/score.csv', header=True)
  df = df_name.join(df_score, on=['Id'], how="left")

  df_name.show()
  df_score.show()

  df_new_column = df.withColumn('NewColumn', F.lit(newValue()))

  df.show()
  df_new_column.show()

  # Case insensitive compare
  df_song = df.filter(F.lower(df['Name']) == 'Song Li'.lower())
  df_song.show()

  path = '/home/song/Sandbox/pyspark-example/files/name-score.csv'

  # df.write.csv(path, header=True)
  df.toPandas().to_csv(path, index=False)

  print(sys.executable)
  
# Run the app
if __name__ == "__main__":
  run()