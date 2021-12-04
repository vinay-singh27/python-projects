import boto3

aws_mng_console = boto3.session.Session(profile_name='root')

#Creating EC2, S3 & IAM objects using Client

iam_mng_console = aws_mng_console.client(service_name= 'iam')
s3_mng_console = aws_mng_console.client(service_name= 's3')
ec2_mng_console = aws_mng_console.client(service_name= 'ec2')

'''
#List all the IAM policies
response = iam_mng_console.list_users()

for item in response['Users']: 
		print(item['UserName'])
 

 #List all the EC2 Instances
'''

#List all the ec2 instances

response = ec2_mng_console.describe_instances()

print(response)

