'''Manual Steps :
1. Go to AWS Management Console
2. Go to IAM Management Console
3. See the IAM users in User option
'''

import boto3
aws_mng_con_root = boto3.session.Session(profile_name='root')
iam_man_con_re = aws_mng_con.resource('iam')
iam_man_con_cli = aws_mng_con.client('iam')

#Using Resource
for each_user in iam_man_con_re.users.all() :
	print(each_user.name)

#Using Client 


