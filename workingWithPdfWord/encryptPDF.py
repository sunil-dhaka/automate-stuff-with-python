from PyPDF2 import PdfFileReader,PdfFileWriter
import sys,os

def encryptPDF(file,password):
    pdfInput=PdfFileReader(file)

    pdfWriter=PdfFileWriter()

    for page in range(pdfInput.getNumPages()):
        pdfWriter.addPage(pdfInput.getPage(page))

    pdfWriter.encrypt(password)
    basepath='/'.join(os.path.abspath(file).split('/')[:-1])
    with open(basepath+'/'+'encrypted'+os.path.abspath(file).split('/')[-1],'wb') as output:
        pdfWriter.write(output)

if __name__=="__main__":
    if len(sys.argv)>2:
        file=sys.argv[1]
        password=sys.argv[2] # 'jamesbond'
        if '.pdf' not in file:
            print('Please give a pdf file')
            sys.exit() 
    else:
        print('Give <file-that-needs-to-be-encrypted> <encryption-password>.')
        sys.exit()

    encryptPDF(file,password)