import boto3
import pandas as pd
from io import StringIO

def lambda_handler(event, context):
    
    client_bucket = 's3clientbucketdemo'
    database_bucket = 's3databasedemo'
    
    #Get details from the Event
    file_location = event['Records'][0]['s3']['object']['key']
    event_time = event['Records'][0]['eventTime']
    
    #Get the Client Name
    client_name = file_location.split('/')[0]
    
    #Creating Pandas Dataframe for the client file
    response = s3.get_object(Bucket=client_bucket, Key= file_location)
    file = response["Body"]
    client_dataframe = pd.read_csv(file, sep = '\t')
    client_dataframe.drop_duplicates(inplace = True)
    
    #QC the client file

    #Checking number of columns provided by the client
    num_of_cols_remarks = []
    if len(dataframe.columns) != 3 :
        num_of_cols_remarks.append('The Number of Columns provided in the text file are not correct. There must be only 3 columns.')

    #Checking the Cycle Column
    cycle_column_remarks = []
    if dataframe.columns[0] != 'Cycle' :
        cycle_column_remarks.append('The Name of the first column provided in the text file is not correct. It must be Cycle(case sensitive).')
    else :    
         if dataframe['Cycle'].nunique() != 1 :
            cycle_column_remarks.append('There are multiple Semester Values in the Cycle Column. Only one semester value must be present in the text file.')
    
         if dataframe['Cycle'].unique()[0].lower() not in ('s219', 's119','s218', 's118','s217', 's117','s216', 's116') :
            cycle_column_remarks.append('The Cycle value is not correct.')  

    #Checking the BU Column
    bu_column_remarks = []
    if dataframe.columns[1] != 'BU' :
        bu_column_remarks.append('The Name of the second column provided in the text file is not correct. It must be BU(case sensitive).')

    else : 
        if dataframe['BU'].nunique() != 1 :
            bu_column_remarks.append('There are multiple Business Unit in the Business Unit Column. It must be either ACM OR AFM')
    
        if dataframe['BU'].unique()[0].lower() not in ('acm', 'afm') :
            bu_column_remarks.append('The Business Unit value is not correct. It must be either ACM OR AFM')  

    #Checking the NPI Column
    npi_column_remarks = []
    if dataframe.columns[2] != 'NPI' :
        npi_column_remarks.append('The Name of the third column provided in the text file is not correct. It must be NPI(case sensitive).')
    #Checking the number of Counts
    count_remark = []
    if dataframe['NPI'].count() > 100000 :
        count_remark.append('The Number of NPIs are greater than 100k. One time request limit is 100k ')
        
    #Final QC Report
    correct_format = len(num_of_cols_remarks) or len(cycle_column_remarks) or len(bu_column_remarks) or len(npi_column_remarks) + len(count_remark)
        
    if correct_format != 0 :
        all_remarks = num_of_cols_remarks + cycle_column_remarks + bu_column_remarks + npi_column_remarks + count_remark
        report = event_time + "report.txt"
        f = open(report, 'w+')
        f.write('The Text File uploaded does not meet the Standard Requirement.Please find below the list of discrepancies in the file.\n')
        count = 1
        for error in all_remarks:
            f.write(f'{count}. {error}\n')
            count += 1
        f.write('\nPlease visit this link www.help.com for the standard documentation of the input file')
        f.close()
        report_name = '/tmp/'+report
        file_loc = client_name + "/Outging/" + report_name 
        s3.meta.client.upload_file(filename = filename , bucket = 's3clientdemobucket', key = file_loc)
        
        
    
    if correct_format == 0 : 
    #Creating Pandas Dataframe for the client avaiable database

    semester = client_dataframe['Cycle'].unique()[0].lower()
    bu = client_dataframe['BU'].unique()[0].lower()
    client_database = str(client_name) + "/" + str(bu) + "/" + semester + "/"
    my_bucket = s3.Bucket('s3databasedemo')
    
    #Looping through all the files present in clients main database
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
