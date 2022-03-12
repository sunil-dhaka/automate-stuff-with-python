import csv,openpyxl,os
# TODO: get values in the place of formulas from excel file
# DONE: use data_only=True in load_workbook
def excel2csv(file):
    file_path_str=os.path.abspath(file).split('/')
    base_path='/'.join(file_path_str[:-1])
    file_name=file_path_str[-1].split('.')[0]
    wb=openpyxl.load_workbook(file,data_only=True)
    sheets=wb.sheetnames
    for sheet in sheets:
        curr_sheet=wb[sheet]
        # if sheet is not empty
        if curr_sheet.max_column>0 and curr_sheet.max_row>0:
            sheet_data=[]
            for row in curr_sheet.rows:
                row_data=[ele.value for ele in row]
                sheet_data.append(row_data)
        with open(f'{base_path}/{file_name}_{sheet}.csv','w') as csv_file:
            file=csv.writer(csv_file)
            file.writerows(sheet_data)
