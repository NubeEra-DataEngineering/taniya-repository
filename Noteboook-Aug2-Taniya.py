# Databricks notebook source
# MAGIC %python
# MAGIC print("Welcome")

# COMMAND ----------

df_remote_table=(spark.read
                 .format("sqlserver")
                 .option("host","server-2aug-taniya.database.windows.net")
                 .option("port","1433")
                 .option("user", "admin123")
                 .option("password","admin@123")
                 .option("database","db-2aug-taniya")
                 .option("dbtable","dbo.iris_data")
                 .load()
                 )

# COMMAND ----------

print(df_remote_table)
