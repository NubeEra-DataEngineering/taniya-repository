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

# COMMAND ----------


access_key = ""

secret_key = ""

 

#Mount bucket on databricks

encoded_secret_key = secret_key.replace("/", "%2F")

aws_bucket_name = "bkt-taniya-4aug"

mount_name = "taniyaawss3"

dbutils.fs.mount("s3a://%s:%s@%s" % (access_key, encoded_secret_key, aws_bucket_name), "/mnt/%s" % mount_name)

display(dbutils.fs.ls("/mnt/%s" % mount_name))


mount_name = "taniyaawss3"

file_name="iris.csv"

df = spark.read.format("csv").load("/mnt/%s/%s" % (mount_name , file_name))




# COMMAND ----------

df.show()
strMountPointParquetFile="/mnt/%s/abc.parquet" % (mount_name)
df.write.parquet(strMountPointParquetFile)
