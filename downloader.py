#-----Downloading Files from the Web with the requests Module-----#

## todo
# add search functionality and then giving top 20(if there are, if zero :notFound) options to choose from
# give stored book name according option choosen
# and then only ask for download  
# after showing some lines ask for full download
# also show size of the data that he will be downloading

import requests

## get the link
#page_link=input()

## simple get data and write into txt file after asking user
r=requests.get('https://www.gutenberg.org/ebooks/66439.txt.utf-8')

# with simple old print function
'''if r.status_code==requests.codes.ok: #checking status
    data=r.text
    print('First 1000 words of your requested text -->\n',data[:1000])
else:
    print('There is some error in fectching requested page.')'''

# with try-exception-else

#################
# Always call `raise_for_status()` after calling requests.get(). You want to be
# sure that the download has actually worked before your program continues.
#################

try:
    r.raise_for_status()
    data=r.text
except Exception as e:
    print('Ohho! Not good at all. There is `your` problem: %s' %e) # using sting replacement by variable into print
else:
    if data==None:
        print('Your link does not have no data')
    else:
        print('OMG! We found your data.')
        checker=0
        while(checker==0):
            answer=input('Want to download your file:(y|N)? ')
            if answer.lower()=='y' or answer.lower()=='yes':
                # write downloaded data into file
                # you need towrite binary data instead of text data in order to maintain the Unicode encoding of the text.
                print('downloading and storing ...')
                book=open('Ebook.txt','wb')
                for data_chunk in r.iter_content(50000):
                    book.write(data_chunk)
                book.close()
                checker=1
            elif answer.lower()=='n' or answer.lower()=='no':
                print('Thank you for trying this downloader. It was a nice book, you should have downloaded :)')
                checker=1
            else:
                print('Please give a vaild input.')

