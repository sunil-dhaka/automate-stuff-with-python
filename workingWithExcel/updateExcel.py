import openpyxl

workbook=openpyxl.load_workbook('produceSales.xlsx')

sheetname=workbook.sheetnames[0]
print(f'working on -- {sheetname}')
sheet=workbook[sheetname]

for i,row in enumerate(sheet.rows):
    # to avoid column name row
    if i>0:
        if row[0].value=='Garlic':
            sheet[f'B{i+1}']=3.07
            sheet[f'D{i+1}']=round(row[1].value*row[2].value,2)
        elif row[0].value=='Celery':
            sheet[f'B{i+1}']=1.19
            sheet[f'D{i+1}']=round(row[1].value*row[2].value,2)
        elif row[0].value=='Lemons':
            sheet[f'B{i+1}']=1.27
            sheet[f'D{i+1}']=round(row[1].value*row[2].value,2)

workbook.save('productSalesUpdated.xlsx')
print('Saved sales file with updated data.')