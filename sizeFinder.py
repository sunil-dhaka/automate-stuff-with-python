import os

def sizeFinder(): # <-- goes pwd
    totalSize=0
    for f in os.listdir():
        if os.path.getsize(f)==4096:
#            print('$$$$')
            os.chdir(f)
 #           print(os.listdir())
            totalSize+= sizeFinder()+4096
            os.chdir('..')
        else:
            totalSize+=os.path.getsize(f)
    return totalSize