from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud, wordcloud
import numpy as np
import requests
import string
from nltk import corpus
import sys
import os

stopwords=corpus.stopwords.words('english')

def wordCloud(fileName,maskImage=None):
    name='-'.join(fileName.split('.')[0].split(' '))

    with open(fileName,'r') as file:
        r=file.readlines()
        text_data=[]
        for line in r:
            foo_data=(line.lower()).strip('\n').split(' ')
            # avoid stopwords -- avoid single characters -- avoid words that have string punctuatoins in them  -- avoid nuber containg words
            text=[str(foo.strip(string.punctuation)) for foo in foo_data if (foo not in stopwords) and (len(foo)>1) and (not any((c in string.punctuation) for c in foo)) and (not any(c.isdigit() for c in foo))]
            text_data.extend(text)
    
    countDict={}
    for ele in text_data:
        countDict[ele]=countDict.get(ele,0)+1

    if maskImage is None:
        wordCloud=WordCloud(background_color='white',width=800, height=400).fit_words(countDict)
    
    else:
        mask_for_cloud=np.array(Image.open(maskImage))
        wordCloud=WordCloud(background_color='white',mask=mask_for_cloud,width=800, height=400).fit_words(countDict)
    
    plt.figure(figsize=(20,16)) # can change sizesusing python og images and plots
    plt.imshow(wordCloud,interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.savefig(name+'.png')
    plt.show()

if len(sys.argv)>1:
    if len(sys.argv)==2:
        if os.path.isfile(sys.argv[1]):
            fileName=sys.argv[1]
        else:
            print(f'{sys.argv[1]} does not exists. Give a valid file name.')
            exit()

    else:
        if os.path.isfile(sys.argv[1]):
            fileName=sys.argv[1]
            if os.path.isfile(sys.argv[2]):
                maskImage=sys.argv[2]
            else:
                print(f'{sys.argv[2]} does not exists. Give a valid file name.')
                exit()
        else:
            print(f'{sys.argv[1]} does not exists. Give a valid file name.')
            exit()
            
    if len(sys.argv)>2:
        wordCloud(fileName,maskImage)
    else:
        wordCloud(fileName)

else:
    print('This can create a word cloud image(800x400[px]) based on .txt file given as first input and second input as mask image.')