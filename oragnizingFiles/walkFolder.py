import os,sys

def folderWalker(folder):
    for rootFolder,subFolder,fileNames in os.walk(folder):
        print(''.center(50,'='))
        print(f'Current folder -- {rootFolder}')
        for sub in subFolder:
            print(f'{sub} is a subfolder of {rootFolder}')
        for subFile in fileNames:
            print(f'{subFile} is a file of {rootFolder}')
        
        print(''.center(50,'='))

if __name__=="__main__":
    if len(sys.argv)>1:
        folder=sys.argv[1]
        # check given path is dir or not
        if not os.path.isdir(folder):
            print('Given is not a folder.')
            sys.exit()
    else:
        print('give folder that needs to be walked')
        sys.exit()
    
    folderWalker(folder)