import csv

def removeHeader(file):
    with open(file,'r') as csv_file:
        file_content=list(csv.reader(csv_file))
    
    with open(file,'w') as csv_file:
        new_csv=csv.writer(csv_file,delimiter=',')
        new_csv.writerows(file_content[1:])
