# Databricks notebook source
dbutils.help()

# COMMAND ----------

dbutils.fs.ls("/tmp/")

# COMMAND ----------

dbutils.fs.put("/tmp/abc.txt","Welcome to Databricks File System",True)

# COMMAND ----------

dbutils.fs.help("mkdirs")

# COMMAND ----------

dbutils.fs.ls("s3://bkt-taniya-4aug/input/iris.csv")
# spark.read.format("parquet").load("s3://bkt-taniya-4aug/input/iris.parquet")



# COMMAND ----------

df=spark.sql("SELECT * FROM parquet.`s3://bkt-taniya-4aug/input/userdata1.parquet`")
df.head()
