import os,sys,shutil

def selectiveCopy(folder,extType,destinationFolder):
    if os.path.exists(destinationFolder) and os.path.isdir(destinationFolder):
        pass
    else:
        os.mkdir(destinationFolder)

    for rootFolder,_,fileNames in os.walk(folder):
        for subFile in fileNames:
            if extType in subFile:
                shutil.copy(rootFolder+'/'+subFile,destinationFolder+'/'+subFile)

if __name__=="__main__":
    if len(sys.argv)>3:
        folder=sys.argv[1]
        ext_type=sys.argv[2]
        dest_folder=sys.argv[3]
        # check given path is dir or not
        if not os.path.isdir(folder):
            print('give valid folder')
            sys.exit()
    else:
        print('input format: <source_folder> <file_extension> <destination_folder>')
        sys.exit()
    
    selectiveCopy(folder,ext_type,dest_folder)