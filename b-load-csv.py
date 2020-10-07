
import sys
from pyspark import SparkContext, SQLContext, SparkConf
from pyspark.sql import Row

def run():
  conf = SparkConf().setAppName('load CSV').setMaster('local[2]')

  context = SparkContext(conf = conf)
  context.setLogLevel('ERROR')
  sqlContext = SQLContext(context)

  df_name = sqlContext.read.csv('/home/song/Sandbox/pyspark-example/files/name.csv', header=True)
  df_score = sqlContext.read.csv('/home/song/Sandbox/pyspark-example/files/score.csv', header=True)
  df = df_name.join(df_score, on=['Id'], how="left")

  df_name.show()
  df_score.show()
  df.show()

  path = '/home/song/Sandbox/pyspark-example/files/name-score.csv'

  # df.write.csv(path, header=True)
  df.toPandas().to_csv(path, index=False)

  print(sys.executable)
  
# Run the app
if __name__ == "__main__":
  run()