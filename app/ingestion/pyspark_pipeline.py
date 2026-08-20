from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DocumentPipeline") \
    .getOrCreate()

df = spark.read.text("data/raw/*.txt")

cleaned_df = df.dropna()

cleaned_df.write.mode(
    "overwrite"
).json("data/processed")
