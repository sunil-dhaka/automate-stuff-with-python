import os

os.makedirs('playground')
os.chdir('playground')
print(os.getcwdb()) #pwd
print(os.getcwd())
print(os.listdir()) #ls
print(os.getcwd())
for f in ['james','bond','is','goind','to','die','like','all/of/us']:
    print(os.path.join(os.getcwd(),f))
print(os.makedirs('james/bond/never/dies')) #<-- does not give any op
print(os.listdir(os.chdir('James'))) 
print(os.listdir(os.chdir('bond')))