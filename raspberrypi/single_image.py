import boto3
from botocore.client import Config
import glob
import datetime
import datetime
import os
ACCESS_KEY_ID = 'AKIAILXA7SJI2JU6UESQ'
ACCESS_SECRET_KEY = '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'
BUCKET_NAME = 'sagemaker-ap-southeast-1-109586776253'
print("Sending images to AWS Cloud")
# send images to cloud

a ='tsunami.jpg'
data = open('tsunami.jpg','rb') 
   
 
s3 = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        config=Config(signature_version='s3v4')
    )

s3.Bucket(BUCKET_NAME).put_object(Key='tsunami.jpg',Body=data)
print("Done")
if(a=='tsunami.jpg'):
   os.system("python sms.py")
   os.system("python3 mail.py")
