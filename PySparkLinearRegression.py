import os, sys
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder
from pyspark.sql.functions import col
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DIRVER_PYTHON'] = sys.executable

spark = SparkSession.builder.master('local[*]').appName("ml_demo").getOrCreate()

df = spark.read.csv("headbrain.csv", header=True)
new_df = df.drop(*['Gender', 'Age Range'])
new_df = new_df.select(*(col(c).cast("Integer").alias(c) for c in new_df.columns))

X = new_df.drop('Brain Weight(grams)')

assembler = VectorAssembler(inputCols=X.columns, outputCol='features')
output = assembler.transform(new_df).select('features', 'Brain Weight(grams)')
regression = LinearRegression(featuresCol='features', labelCol='Brain Weight(grams)')

regression_model = regression.fit(output)
# regression_model.coefficients
# regression_model.intercept

test_data = [(4512.0,),(4011.0,)]
rdd = spark.sparkContext.parallelize(test_data)
col_name = ['Head Size(cm^3)']
test_df = spark.createDataFrame(rdd).toDF(*col_name)

test_assembler = VectorAssembler(inputCols=test_df.columns, outputCol='features')
test_output = assembler.transform(test_df).select('features')
# test_output.show()
test_op = regression_model.transform(test_output)
# test_op.show()
