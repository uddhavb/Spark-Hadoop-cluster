from pyspark import SparkConf, SparkContext
from pyspark.sql import SQLContext, Row, SparkSession
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
sc = SparkContext()
import sys
sqlContext = SQLContext(sc)
spark = SparkSession.builder.appName("Rating").getOrCreate()
#df_bus = sqlContext.createDataFrame(sc.textFile('hdfs://157.230.1.136:9000/yelp_business.csv').map(lambda line: line.split(",")))
df_bus = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferSchema='true').load('hdfs://157.230.1.136:9000/yelp_business.csv')
#df_bus = spark.read.text('hdfs://157.230.1.136:9000/yelp_business.csv').cache()
df_bus_att = sqlContext.createDataFrame(sc.textFile('hdfs://157.230.1.136:9000/yelp_business_attributes_format.csv').map(lambda line: line.split(",")))
df_checkin = sqlContext.createDataFrame(sc.textFile('hdfs://157.230.1.136:9000/yelp_checkin.csv').map(lambda line: line.split(",")))

df_bus.show(5)
#print(df_bus.columns)
#print(df_bus_att.columns)

df_bus.registerTempTable("business_table")
df_bus.printSchema()                                                                                                                                                                           
places = sqlContext.sql("select distinct city from business_table")
#places=np.unique(np.array(sqlContext.sql("SELECT city FROM business_table")))
#places = np.unique(np.array(df_bus['city']))

for place in places.collect():
        print(place)

search = str(sys.argv[1])
print(search)
sqlContext.sql("select count(`name`) from business_table group by city having city='"+search+"'").show()
sqlContext.sql("select name from business_table where city='"+search+"' and stars=(select max(stars) from business_table group by city having city='"+search+"')").show()
