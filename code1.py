from pyspark import SparkContext
from pyspark.sql import SQLContext
import pandas as pd




sc = SparkContext('local','example')  # if using locally
df_business=sc.textFile('yelp_business.csv')
df_business_Attributes=sc.textFile('yelp_business_attributes.csv')
df_hours=sc.textFile('yelp_business_hours.csv')
df_checkin=sc.textFile('yelp_checkin.csv')

print("Collecting Business Data and printing")
print(df_business.collect())

print("Collecting Business attributes data and printing")
print(df_business_Attributes.collect())


print("Collecting Business hours data and printing")
print(df_hours.collect())

print("COllecting Checkin Data and printing")
print(df_checkin.collect())


