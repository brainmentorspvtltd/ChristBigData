import os, sys
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, OneHotEncoder
from pyspark.sql.functions import col
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler

import streamlit as st

st.title("Streamlit Taking Input Example")
st.write("Simple Example to take input from user...")

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DIRVER_PYTHON'] = sys.executable

spark = SparkSession.builder.master('local[*]').appName("ml_demo_2").getOrCreate()

@st.cache(suppress_st_warning=True)
def do_prediction(headSize):

    df = spark.read.csv("headbrain.csv", header=True)
    new_df = df.drop(*['Gender', 'Age Range'])
    new_df = new_df.select(*(col(c).cast("Integer").alias(c) for c in new_df.columns))

    X = new_df.drop('Brain Weight(grams)')

    assembler = VectorAssembler(inputCols=X.columns, outputCol='features')
    output = assembler.transform(new_df).select('features', 'Brain Weight(grams)')
    regression = LinearRegression(featuresCol='features', labelCol='Brain Weight(grams)')

    regression_model = regression.fit(output)
    st.write("Coeff : {}".format(regression_model.coefficients))
    st.write("Intercept : {}".format(regression_model.intercept))

    test_data = [(headSize,)]
    rdd = spark.sparkContext.parallelize(test_data)
    col_name = ['Head Size(cm^3)']
    test_df = spark.createDataFrame(rdd).toDF(*col_name)

    test_assembler = VectorAssembler(inputCols=test_df.columns, outputCol='features')
    test_output = assembler.transform(test_df).select('features')
    # test_output.show()
    test_op = regression_model.transform(test_output)
    # st.write(str(test_op.show()))
    st.write("Prediction is {}".format(str(test_op.collect()[0][1])))

form = st.form(key = "my_form")
headSize = form.text_input(label="Enter Head Size : ")
submit = form.form_submit_button(label="Predict Brain Weight...")

if submit:
    st.write("Head Size is {}".format(headSize))
    do_prediction(int(headSize))
    