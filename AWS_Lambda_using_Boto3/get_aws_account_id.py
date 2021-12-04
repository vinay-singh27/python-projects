import boto3

#Creating AWS Management Console

aws_mng_con_root =boto3.session.Session(profile_name= 'root')

sts_mng_console = aws_mng_con_root.client(service_name = 'sts')
response = sts_mng_console.get_caller_identity()
print(response)