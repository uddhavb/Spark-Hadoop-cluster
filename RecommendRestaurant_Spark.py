import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree

from pyspark import SparkContext
sc = SparkContext()
from pyspark.sql import SQLContext, Row
sqlContext = SQLContext(sc)

df_bus = sqlContext.createDataFrame(sc.textFile('hdfs://157.230.1.136:9000/yelp_business.csv').map(lambda line: line.split(",")))
df_bus_att = sqlContext.createDataFrame(sc.textFile('hdfs://157.230.1.136:9000/yelp_business_attributes.csv').map(lambda line: line.split(",")))
df_checkin = sqlContext.createDataFrame(sc.textFile('hdfs://157.230.1.136:9000/yelp_checkin.csv').map(lambda line: line.split(",")))


#print(df_bus.columns)
#print(df_bus_att.columns)

documents.registerTempTable("business_table")
places=np.unique(np.array(sqlContext.sql("SELECT city FROM business_table")))
print(places)
place=input('select a place among the following')

if(place in places):
    df_by_places=df_bus.groupby('city')
    for i,j in df_by_places:
        if(i==place):
            #print(j)
            print('The best Restaurant(s) in this area is ')
            best_rest=j
            name_stars=best_rest[best_rest['stars']==best_rest['stars'].max()]
            print(name_stars['name'])
