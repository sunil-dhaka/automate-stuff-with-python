import os

def sizeFinder(): # <-- goes pwd
    totalSize=0
    for f in os.listdir():
        if os.path.isdir(f):
            os.chdir(f)
            totalSize+= sizeFinder()+4096
            os.chdir('..')
        else:
            totalSize+=os.path.getsize(f)
    return totalSize