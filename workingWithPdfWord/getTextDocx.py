import docx,sys,os

def getText(file):
    doc=docx.Document(file)

    text=''
    for para in doc.paragraphs:
        text+=para.text+'\n'
    
    path_struc=os.path.abspath(file).split('/')
    with open('/'.join(path_struc[:-1])+'/'+path_struc[-1].split('.')[0]+'.txt','w') as f:
        f.write(text)

if __name__=="__main__":
    if len(sys.argv)>1:
        file=sys.argv[1]
        if '.docx' not in file:
            print('Please give a docx file')
            sys.exit() 
    else:
        print('Give <file-that-needs-to-be-extracted>.')
        sys.exit()

    getText(file,)