from PyPDF2 import PdfFileReader, PdfFileWriter
import sys,os
from time import time

dict_file_path='/home/sunild/Downloads/gits/automate-stuff-with-python/workingWithPdfWord/files/dictionary.txt'
with open(dict_file_path,'r') as file:
    tmp_dict=[line.strip() for line in file.readlines()]
DICT=[]
for password in tmp_dict:
    DICT.append(password)
    DICT.append(password.lower())

def jailBreak(file):
    pdfInput=PdfFileReader(file)

    if pdfInput.isEncrypted:
        decrypted=0
        for password in DICT:
            if pdfInput.decrypt(password):
                print(f'Password is \"{password}\".')
                decrypted=1
                break
        if decrypted:
            pdfWriter=PdfFileWriter()
            for page in range(pdfInput.getNumPages()):
                pdfWriter.addPage(pdfInput.getPage(page))

            path_struc=os.path.abspath(file).split('/')
            with open('/'.join(path_struc[:-1])+'/'+path_struc[-1].split('.')[0]+'decrypted'+'.pdf','wb') as f:
                pdfWriter.write(f)

            return 1
        else:
            return 0
    else:
        pdfWriter=PdfFileWriter()
        for page in range(pdfInput.getNumPages()):
            pdfWriter.addPage(pdfInput.getPage(page))

        path_struc=os.path.abspath(file).split('/')
        with open('/'.join(path_struc[:-1])+'/'+path_struc[-1].split('.')[0]+'decrypted'+'.pdf','wb') as f:
            pdfWriter.write(f)

        return 1


if __name__=="__main__":
    if len(sys.argv)>1:
        file=sys.argv[1]
        if '.pdf' not in file:
            print('Please give a pdf file')
            sys.exit() 
    else:
        print('Give <file-that-needs-to-be-jailbreaked>.')
        sys.exit()
    tic=time()
    is_breaked=jailBreak(file)
    toc=time()
    if is_breaked:
        print(f'Jailbreaked in {round(toc-tic,2)} seconds.')
    else:
        print('Nice. File is strongly encrypted for this dictionary. Couldn\'t jailbreak.')