import boto3
import pandas as pd
import s3fs

aws_mng_con_root =boto3.session.Session(profile_name= 'root')
s3 = aws_mng_con_root.resource(service_name = 's3')

client_name = "Client1"
event_time = "2020-02-23T09:30:22.871Z"
filename = 'test_npi_list.txt'

'''
#Source location of the file
copy_source = { 'Bucket': 's3clientbucketdemo',
                'Key': 'Client1/Incoming/test_npi_list.txt'}

#s3://s3clientbucketdemo/Client1/Incoming/test_npi_list.txt

#Creating Destination Folder
dest_folder = "Requests/" + str(client_name) + "/" + str(event_time) + "/"
s3.meta.client.put_object(Bucket='s3databasedemo', Key=dest_folder)

#Copying the File
s3.meta.client.copy(copy_source, 's3databasedemo', dest_folder)

print('Job Done')

'''

#Creating Pandas Dataframe for the client file
#client_file = "Requests/" + str(client_name) + "/" + str(event_time) + "/" + filename

#Directly taking file from client folder


response = s3.get_object(Bucket="s3clientbucketdemo",Key= 'Client1/Incoming/test_npi_list.txt')
file = response["Body"]

Dataframe = pd.read_csv(file, sep = '\t')

client_dataframe = pd.read_csv('s3://s3clientbucketdemo/Client1/Incoming/test_npi_list.txt')
print(Dataframe.count()





