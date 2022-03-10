import os,sys,send2trash

def deleteMassiveFiles(folder,sizeThersold):
    for rootFolder,_,fileNames in os.walk(folder):
        for subFile in fileNames:
            file_size=round(os.path.getsize(rootFolder+'/'+subFile)/(1024*1024))
            if file_size>sizeThersold:
                print(f'removing {subFile} with file size {file_size} MB')
                send2trash.send2trash(f'{rootFolder}/{subFile}')

if __name__=="__main__":
    if len(sys.argv)>2:
        folder=sys.argv[1]
        size_thers=float(sys.argv[2])
        # check given path is dir or not
        if not os.path.isdir(folder):
            print('give valid folder')
            sys.exit()
    else:
        print('input format: <source_folder> <size_thersold>')
        sys.exit()
    
    deleteMassiveFiles(folder,size_thers)