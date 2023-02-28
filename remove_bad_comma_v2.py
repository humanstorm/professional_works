# %%
#import csv
import pandas as pd
import os
import re
from datetime import datetime
import glob

# %%
#data = pd.read_csv("C:\\Users\\Reporting\\Documents\\source\\2023_02_ 21_1133PM_TMW_UserHistory.csv", encoding='cp1252')
''' to find all file within a folder that are .csv. if it is report[0-9].csv then convert it into column_name.csv with time stamp.
    Replace some bad comma in few columns
    Remove column_name & column_name column  '''
#change current working directory
os.chdir(r'C:\Automated')
file_list = glob.glob('./xlsx/*.csv')

try: 
    if os.path.isfile(file_list[0]):
        #get file name
        input_file = file_list[0]
        print(input_file)
        output_file = os.path.basename(input_file)
        
        #create timestamp
        today = datetime.now()
        dt_string = today.strftime("%Y_%m_%d_%H%M%p")
        
        #naming new file if input file is report.
        if bool(re.match(r"report[0-9]+\.csv+", output_file)) == True:
            output_file = dt_string + r'_filename.csv'

        #read csv file
        data = pd.read_csv(input_file, encoding='utf8',on_bad_lines='skip',dtype='unicode')

        #remove columns & replace bad comma
        data['column_name'].replace(to_replace='\,',value=' ', regex=True,inplace=True)
        data['column_name2'].replace(to_replace='\,',value=' ', regex=True,inplace=True)
        data['column_name'].replace(to_replace='\,',value=' ', regex=True,inplace=True)
        data['column_name'].replace(to_replace='\,',value=' ', regex=True,inplace=True)
        data.drop(columns=['column_name','column_name'],inplace=True)

        #create full file path
        fullname = os.path.join(r'./outbox/', output_file)   
        #extract to csv file
        data.to_csv(fullname,index=False)

        os.remove(input_file)
except IndexError:
        pass





