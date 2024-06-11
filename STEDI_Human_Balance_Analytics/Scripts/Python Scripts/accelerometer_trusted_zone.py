import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1716932710451 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_landing", transformation_ctx="AmazonS3_node1716932710451")

# Script generated for node Amazon S3
AmazonS3_node1716932706818 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="customer_trusted", transformation_ctx="AmazonS3_node1716932706818")

# Script generated for node Customer Privacy Filter
CustomerPrivacyFilter_node1716932894847 = Join.apply(frame1=AmazonS3_node1716932710451, frame2=AmazonS3_node1716932706818, keys1=["user"], keys2=["email"], transformation_ctx="CustomerPrivacyFilter_node1716932894847")

# Script generated for node Drop Fields
DropFields_node1716933233434 = DropFields.apply(frame=CustomerPrivacyFilter_node1716932894847, paths=["customername", "email", "phone", "birthdate", "serialnumber", "registrationdate", "lastupdatedate", "sharewithresearchasofdate", "sharewithpublicasofdate"], transformation_ctx="DropFields_node1716933233434")

# Script generated for node Amazon S3
AmazonS3_node1716933173025 = glueContext.getSink(path="s3://paw-lake-house/accelerometer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1716933173025")
AmazonS3_node1716933173025.setCatalogInfo(catalogDatabase="stedi",catalogTableName="accelerometer_trusted")
AmazonS3_node1716933173025.setFormat("json")
AmazonS3_node1716933173025.writeFrame(DropFields_node1716933233434)
job.commit()
