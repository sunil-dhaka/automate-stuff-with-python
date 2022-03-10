import os,zipfile,sys

def backupFolder2Zip(folder):
    zip_name=os.path.abspath(folder).split('/')[-1]
    # already_there_zips=[file for file in os.listdir(folder) if '.zip' in file and zip_name in file]
    zip_file=zipfile.ZipFile(zip_name+'.zip','w')
    for rootFolder,subFolder,fileNames in os.walk(folder):
        # write empty folders
        for sub in subFolder:
            zip_file.write(rootFolder+'/'+sub,compress_type=zipfile.ZIP_DEFLATED)
        # write files from folders
        for subFile in fileNames:
            zip_file.write(rootFolder+'/'+subFile,compress_type=zipfile.ZIP_DEFLATED)
    
    zip_file.close()

if __name__=="__main__":
    if len(sys.argv)>1:
        folder=sys.argv[1]
        if not os.path.isdir(folder):
            print('Given is not a folder.')
            sys.exit()
    else:
        print('give folder that needs to be zipped')
        sys.exit()
    
    backupFolder2Zip(folder)