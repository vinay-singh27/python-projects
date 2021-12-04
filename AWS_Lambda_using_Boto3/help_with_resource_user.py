import boto3

aws_mng_console = boto3.session.Session(profile_name='root')

#Creating EC2, S3 & IAM objects using Resource Object

iam_mng_console = aws_mng_console.resource(service_name= 'iam')
s3_mng_console = aws_mng_console.resource(service_name= 's3')
ec2_mng_console = aws_mng_console.resource(service_name= 'ec2')

iam_mng_console.users.all()

for each_item in s3_mng_console.buckets.all() :
	print(dir(each_item))




