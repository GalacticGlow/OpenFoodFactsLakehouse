#example on how to use the config.share file to access the data lakehouse's data
import delta_sharing
from pyspark.sql import SparkSession

profile_file = r"C:\path\to\the\config\config.share"

'''
#how to inspect schema and tables of the share
client = delta_sharing.SharingClient(profile_file)

shares = client.list_shares()
share = shares[0]

schemas = client.list_schemas(share)
schema = schemas[0]
tables = client.list_tables(schema)
'''

table_url = f"{profile_file}#openfoodfacts_share.gold.fact_product_entries_ext"

spark = SparkSession.builder \
    .appName("openfoodfacts") \
    .master("local[*]") \
    .config("spark.jars.packages", "io.delta:delta-sharing-spark_2.12:3.1.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

df = spark.read.format("deltaSharing").load(table_url)

df.printSchema()
df.show(20)