import os
import sizeFinder

os.chdir('playground/')
print(os.getcwd())
base=os.getcwd()
print(os.listdir())
print(os.path.dirname('g1'))
# have to iterate over directories recursively to get whole size including
print(os.getcwd())
print(sizeFinder.sizeFinder())
print(os.path.getsize('file1.txt'))
print(os.path.getsize('g1/file1.txt'))
print(os.path.getsize('g1'))
totalSize=0
for f in os.listdir():
    totalSize+=os.path.getsize(f)

print(totalSize)