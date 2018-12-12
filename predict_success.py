from pyspark import SparkContext

from pyspark.mllib.tree import DecisionTree, DecisionTreeModel
from pyspark.mllib.util import MLUtils

from pyspark.sql import SQLContext, Row, SparkSession

sc = SparkContext()
sqlContext = SQLContext(sc)
business_data = sqlContext.read.format('com.databricks.spark.csv').options(header='true', inferSchema='true').load('hdfs://157.230.1.136:9000/yelp_business.csv')
from pyspark.mllib.regression import LabeledPoint
from pyspark.sql.functions import col
business_data = business_data.select([col(c).cast("float") for c in business_data.columns])
business_data = business_data.rdd
business_data = business_data.map(lambda line: LabeledPoint(line[-4],[line[0:-5]]))
print (business_data.take(1))

(trainingData, testData) = business_data.randomSplit([0.8, 0.2])

model = DecisionTree.trainClassifier(trainingData, numClasses=8, categoricalFeaturesInfo={},impurity='gini', maxDepth=7, maxBins=32)

predictions = model.predict(testData.map(lambda x: x.features))
labelsAndPredictions = testData.map(lambda lp: lp.label).zip(predictions)
testErr = labelsAndPredictions.filter(
    lambda lp: lp[0] != lp[1]).count() / float(testData.count())
print('Test Error = ' + str(testErr))
