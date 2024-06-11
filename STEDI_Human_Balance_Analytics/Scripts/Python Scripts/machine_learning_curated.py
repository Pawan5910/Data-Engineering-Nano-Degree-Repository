import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node Accelerometer trusted
Accelerometertrusted_node1717365371234 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="accelerometer_trusted", transformation_ctx="Accelerometertrusted_node1717365371234")

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1717365372399 = glueContext.create_dynamic_frame.from_catalog(database="stedi", table_name="step_trainer_trusted", transformation_ctx="StepTrainerTrusted_node1717365372399")

# Script generated for node SQL Query
SqlQuery1016 = '''
SELECT
    act.timestamp,
    act.x,
    act.y,
    act.z,
    stt.serialnumber, 
    stt.sensorreadingtime, 
    stt.distancefromobject 
FROM 
    act
JOIN 
    stt 
ON 
    act.timestamp = stt.sensorreadingtime;
'''
SQLQuery_node1717365452128 = sparkSqlQuery(glueContext, query = SqlQuery1016, mapping = {"act":Accelerometertrusted_node1717365371234, "stt":StepTrainerTrusted_node1717365372399}, transformation_ctx = "SQLQuery_node1717365452128")

# Script generated for node Amazon S3
AmazonS3_node1717365520497 = glueContext.getSink(path="s3://paw-lake-house/step_trainer/curated/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1717365520497")
AmazonS3_node1717365520497.setCatalogInfo(catalogDatabase="stedi",catalogTableName="machine_learning_curated")
AmazonS3_node1717365520497.setFormat("json")
AmazonS3_node1717365520497.writeFrame(SQLQuery_node1717365452128)
job.commit()
