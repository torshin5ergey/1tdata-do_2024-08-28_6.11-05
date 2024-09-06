"""
pyspark-script.py - Reads data from PostgreSQL and ClickHouse tables.


"""

import logging
log = logging.getLogger(__name__)

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import clickhouse_connect

def read_from_postgres():
    """Connect to PostgreSQL using JDBC."""
    spark = SparkSession \
        .builder \
        .appName("PostgreSQL") \
        .config("spark.jars", "./postgresql-42.7.4.jar") \
        .getOrCreate()
    spark.sparkContext.setLogLevel("OFF")
    df = spark.read \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://localhost:5432/postgres") \
        .option("dbtable", "employees") \
        .option("user", "postgres") \
        .option("password", "mysecretpassword") \
        .option("driver", "org.postgresql.Driver") \
        .load()
    
    return df

def read_from_clickhouse():
    """Connect using clickhouse-connect."""
    client = clickhouse_connect.get_client(
        host='localhost',
        port=8123,
        username='default',
        password='')
    result = client.query('SELECT * FROM employees')
    schema = StructType([
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("age", IntegerType(), True),
        StructField("salary", IntegerType(), True)
    ])
    # convert 'result' (tuple) to 
    rows = [tuple(row) for row in result.result_rows]
    spark = SparkSession.builder.appName("ClickHouse").getOrCreate()
    #spark.sparkContext.setLogLevel("OFF")
    df = spark.createDataFrame(rows, schema)
    return df


def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(message)s'
    )
    df_pg = read_from_postgres()
    log.info("Данные из PostgreSQL:")
    df_pg.show()
    df_ch = read_from_clickhouse()
    log.info("Данные из ClickHouse:")
    df_ch.show()

if __name__ == "__main__":
    main()
