event = {'Records': [{'eventVersion': '2.1', 
                     'eventSource': 'aws:s3', 
                      'awsRegion': 'us-east-2', 
                      'eventTime': '2020-02-23T09:30:22.871Z', 
                      'eventName': 'ObjectCreated:Put', 
                      'userIdentity': {'principalId': 'A3QSE55GKIQ6LI'}, 
                      'requestParameters': {'sourceIPAddress': '43.239.54.134'}, 
                      'responseElements': {'x-amz-request-id': '2CCAE3D8A67A26A0', 
                                'x-amz-id-2': 'wbW5qhzX1UZAhWXGNYJVUqHFKyGXW39bzbkrhzlJHUwZqWkNj1jJIoEVvVZZ3xEt5MDwBLG7WMt7QMD1H0H/z+rfGRkJEfA/'},
                       's3': {'s3SchemaVersion': '1.0', 
                               'configurationId': '1d2a2199-b0a6-4203-931a-2f961b5827c9', 
                               'bucket': {'name': 's3clientbucketdemo', 
                               'ownerIdentity': {'principalId': 'A3QSE55GKIQ6LI'}, 
                               'arn': 'arn:aws:s3:::s3clientbucketdemo'}, 
                               'object': {'key': 'Client1/Incoming/test_npi_list.txt', 
                                          'size': 34, 
                                          'eTag': 'b8ec26e7ae8e20e9aff1224534a0c9b3', 
                                          'sequencer': '005E52462ED5EDD616'}}}]}

bucket_name = event['Records'][0]['s3']['bucket']['name']
event_time = event['Records'][0]['eventTime']
file_location = event['Records'][0]['s3']['object']['key']
client_name = file_location.split('/')[0]
file_name = file_location.split('/')[2]  
print(bucket_name)
print(event_time)  
print(file_location)    
print(client_name) 
print(file_name)                    

