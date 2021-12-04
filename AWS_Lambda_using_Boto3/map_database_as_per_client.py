import boto3
import pandas as pd
from io import StringIO

aws_mng_con_root =boto3.session.Session(profile_name= 'root')
s3 = aws_mng_con_root.resource(service_name = 's3')
correct_format = 0
if correct_format == 0 : 
	#Creating Pandas Dataframe for the client avaiable database

	#semester = client_dataframe['Cycle'].unique()[0].lower()
	#bu = client_dataframe['BU'].unique()[0].lower()
	#client_name = Client1

	semester = 's219'
	client_name = 'Client1'
	bu = 'acm'

	client_database = str(client_name) + "/" + str(bu) + "/" + semester + "/"

	my_bucket = s3.Bucket('s3databasedemo')

	client_main_database = pd.DataFrame()

	for my_bucket_object in my_bucket.objects.filter(Prefix= client_database):
		file_name = my_bucket_object.key.split('/')[3]

		if file_name != '' :
			file_location = client_database + file_name
			response = s3.meta.client.get_object(Bucket = 's3databasedemo', Key = file_location)
			file = response['Body']
			client_sub_database = pd.read_csv(file, sep = '\t')
			frame = [client_main_database, client_sub_database]
			client_main_database = pd.concat(frame)


	final_table = client_dataframe.merge(client_main_database, on = 'NPI', how = 'left' )
	final_table.fillna('')

	csv_buffer = StringIO()
	final_table.to_csv(csv_buffer, sep = '/t', index = False)
	final_output_file_name = client_name + "/Outgoing/" + event_time + "_output.txt" 
	s3.Object('s3clientbucketdemo', final_output_file_name).put(Body=csv_buffer.getvalue())





