# Código para ser executado no AWS Glue - Spark 2.4 - Python 3

# Libs utilizadas
import sys
from pyspark.context import SparkContext
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: ['JOB_NAME']
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

## definição do contexto para recuperar a seção Spark
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

## definição do Job
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


## Conversão do CVS -> parquet

## Lendos dados do censo
enem = (
    spark
    .read
    .format('CSV')
    .option('header', True)
    .option('inferSchema', True)
    .option('delimiter', '|')
    .load('s3://datalake-smedina-4343-igti-edc/raw-data/censo/')
)

## Escrever no DataLake em parquet
(
    enem
    .write
    .mode('overwrite')
    .format('parquet')
    .partitionBy('CO_UF')
    .save('s3://datalake-smedina-4343-igti-edc/consumer-zone/censo/')
)

