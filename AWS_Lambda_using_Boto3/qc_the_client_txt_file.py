import pandas as pd
dataframe = pd.read_csv(r'C:\Users\Vinay\Desktop\boto3_codes\test_npi_list.txt', sep= '\t')

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
    report_name = event_time + "report.txt"
    f = open(report_name, 'w+')
    f.write('The Text File uploaded does not meet the Standard Requirement.Please find below the list of discrepancies in the file.\n')
    count = 1
    for error in all_remarks:
        f.write(f'{count}. {error}\n')
        count += 1
    f.write('\nPlease visit this link www.help.com for the standard documentation of the input file')
    f.close()
    filename = '/tmp/'+report_name
    file_loc = client_name + "/Outging/" + report_name 
    s3.meta.client.upload_file(filename = filename , bucket = 's3clientdemobucket', key = file_loc)
    
