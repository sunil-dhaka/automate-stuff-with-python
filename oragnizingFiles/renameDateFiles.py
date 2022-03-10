import os,sys,shutil,re

def renameDateFiles(folder):
    regex=re.compile(r'^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-(\d\d\d\d)(.*?)$')
    for rootFolder,subFolder,fileNames in os.walk(folder):
        for subFile in fileNames:
            regex_results=regex.search(subFile)
            # check whether American date formate is in file-name
            if regex_results is None:
                continue
            new_name=regex_results.group(1)+regex_results.group(4)+'-'+regex_results.group(2)+'-'+regex_results.group(6)+regex_results.group(7)
            print(f'moving file {subFile} to {new_name}')
            # uncomment below line to really move/rename files
            # shutil.move(rootFolder+'/'+subFile,rootFolder+'/'+new_name)

if __name__=="__main__":
    if len(sys.argv)>1:
        folder=sys.argv[1]
        # check given path is dir or not
        if not os.path.isdir(folder):
            print('input is not a folder.')
            sys.exit()
    else:
        print('input folder is missing')
        sys.exit()
    
    renameDateFiles(folder)

# TODO: revise regex concepts via a cheatsheet