# Databricks notebook source
storage_account="sataniyav1"
container_name="v1-container-2aug-taniya"
source_url="wasbs://{0}@{1}.blob.core.windows.net".format(container_name, storage_account)

access_key="/tZ7exkUHusRPCPzs6D06J3WbljYfiYU07Q4gu3qVwXStMr/TCn+g6KboxtN36TDhputFc3rdZ81+ASt/Z6K6w=="
mount_point_url="/mnt/gen1dataset"

extra_configs_key=f"fs.azure.account.key.{storage_account}.blob.core.windows.net"
extra_configs_value=access_key
# extra_configs_dict={extra_configs_key:extra_configs_value}


# COMMAND ----------

dbutils.fs.mount(source=source_url,
                 mount_point=mount_point_url,
                 extra_configs={extra_configs_key:extra_configs_value}
                 )
