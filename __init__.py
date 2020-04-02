import csv 
import pandas as pd
import numpy as np
from array import array
from pip._vendor.webencodings import labels

with open('ACS_08_3YR_S1903.csv', 'r') as csv_file:
      
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    df = pd.DataFrame(csv_file, index=labels)
    rows=len(df.axes[0])
    col=len(df.axes[1])
    print("Number of Rows: "+str(rows))
    print("Number of Columns: "+str(col))
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]}', f'\t{row[1]}', f'\t{row[2]}')
#             line_count += 1
#     
#     print(f'Number of rows: {line_count}.')
#     #To print type of a variable:
#     print(type(csv_reader))
#     
#     
#     for line in csv_file.readlines():
#         array = line.split(',')
#     
#     print('Number of columns:',  len(array))
#     
#       