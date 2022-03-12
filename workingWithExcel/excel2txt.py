import openpyxl,sys,os

FOLDER='excel2txt'
def excel2txt(file):
    wb=openpyxl.load_workbook(file)
    sheet=wb[wb.sheetnames[0]]
    
    for i,col in enumerate(sheet.columns):
        col_values=[c.value for c in col]
        with open(FOLDER+'/'+col_values[0]+'.txt','w') as f:
            f.write('\n'.join(col_values[1:]))

if __name__=="__main__":
    if len(sys.argv)>1:
        file=sys.argv[1]
    else:
        print('Give file that contains files in excel format.')
        sys.exit()

    excel2txt(file)