from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as f
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType, BooleanType
import os, zipfile

spark_jars_packages = ",".join(
        [
            "org.postgresql:postgresql:42.4.0",
        ]
    )

def spark_init(task_name : str) -> SparkSession:

    spark = SparkSession.builder\
        .master("local")\
        .appName(task_name)\
        .config("spark.jars.packages", spark_jars_packages)\
        .getOrCreate()

    return spark

def unzip_files() -> None:
    dir_name = '/data'

    files=os.listdir(dir_name)
    for file in files:
        if file.endswith('.zip'):
            filePath=dir_name+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            zip_file.extractall(dir_name)
            zip_file.close()             

def load(spark: SparkSession) -> DataFrame:

    df = spark.read\
        .option("multiline","true")\
        .json("/data/*.json")    

    return df

def save_df(spark: SparkSession, df: DataFrame) -> None:

    df.write \
            .mode("overwrite")\
            .format('jdbc') \
            .option('url', 'jdbc:postgresql://:5432/de') \
                    .option('driver', 'org.postgresql.Driver') \
                    .option('dbtable', 'staging.events') \
                    .option('user', 'jovyan') \
                    .option('password', 'jovyan') \
                    .save()

spark = spark_init('load_staging')

unzip_files()

source_df = load(spark)

save_df(spark, source_df)
