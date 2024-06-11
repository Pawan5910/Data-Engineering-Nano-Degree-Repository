import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import re

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Amazon S3
AmazonS3_node1716668436260 = glueContext.create_dynamic_frame.from_options(format_options={"multiline": False}, connection_type="s3", format="json", connection_options={"paths": ["s3://paw-lake-house/customer/landing/"], "recurse": True}, transformation_ctx="AmazonS3_node1716668436260")

# Script generated for node Privacy Filter
PrivacyFilter_node1716668958016 = Filter.apply(frame=AmazonS3_node1716668436260, f=lambda row: (not(row["shareWithResearchAsOfDate"] == 0)), transformation_ctx="PrivacyFilter_node1716668958016")

# Script generated for node Trusted Customer Zone
TrustedCustomerZone_node1716668980693 = glueContext.getSink(path="s3://paw-lake-house/customer/trusted/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="TrustedCustomerZone_node1716668980693")
TrustedCustomerZone_node1716668980693.setCatalogInfo(catalogDatabase="stedi",catalogTableName="customer_curated")
TrustedCustomerZone_node1716668980693.setFormat("json")
TrustedCustomerZone_node1716668980693.writeFrame(PrivacyFilter_node1716668958016)
job.commit()
