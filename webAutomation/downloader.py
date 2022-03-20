#-----Downloading Files from the Web with the requests Module-----#

## todo
# add search functionality and then giving top 20(if there are, if zero :notFound) options to choose from:: done
# give stored book name according option choosen:: done
# and then only ask for download:: done
# after showing some lines ask for full download:: done
# show book type to download option for choosen book:: have to parse book choosen page and get info

# required modules
import requests
from bs4 import BeautifulSoup as bs
from PyInquirer import prompt

# query input
query=input('what is your query for PG --> ')

r=requests.get('https://www.gutenberg.org/ebooks/search/?query='+query)
if r.status_code==requests.codes.ok:
    print('We were able to search for your query.')
    soup=bs(r.text,features='html.parser')
    if len(soup.find_all('li',{'class':'booklink'}))<1:
        print('your query does not have any results on PG.')
    else:
        #bookshelves_page=[]
        book_name=[]
        book_link=[]
        book_cover_link=[]
        author=[]
        downloads_count=[]
        for book in soup.find_all('li',{'class':'booklink'}):
            #bookshelves_page.append(bookshelves_pages_titles[i])
            book_link.append(book.find('a').get('href').split('/')[-1])
            if book.find('img') != None:
                book_cover_link.append('https://www.gutenberg.org'+book.find('img').get('src'))
            else:
                book_cover_link.append('notFound')
            if book.find('span',{'class':'title'}) != None:
                book_name.append(book.find('span',{'class':'title'}).string)
            else:
                book_name.append('notFound')
            if book.find('span',{'class':'subtitle'}) != None:
                author.append(book.find('span',{'class':'subtitle'}).string)
            else:
                author.append('notFound')
            if book.find('span',{'class':'extra'}) != None:
                downloads_count.append(book.find('span',{'class':'extra'}).string.split(' ')[0])
            else:
                downloads_count.append('notFound')
        book_promp_message=[]
        for i in range(len(book_name)):
            book_promp_message.append(str(i+1).zfill(2)+' ) Book -- '+book_name[i]+' -- by author -- '+author[i])
        #used from search.py
        which_book=[
                {
                    'type':'list',
                    'name':'type',
                    'message':'please choose a book:',
                    'choices':book_promp_message,
                    'default':0
                }
            ]
        print('We found', len(book_promp_message) ,'results. Choose -->')
        answer=prompt(which_book)
        book_no=int(answer['type'][:2])-1
        book_id=book_link[book_no]
        ## get the link
        link='https://www.gutenberg.org/cache/epub/'+book_id+'/pg'+book_id+'.txt'

        ## simple get data and write into txt file after asking user
        r=requests.get(link)

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
                        print('Initial lines -->\n',data[:1000])
                        want_to=input('Is this the book:(y|N)? ')
                        if want_to.lower()=='y' or want_to.lower()=='yes':
                            print('downloading and storing ...')
                            book=open(book_name[book_no]+'.txt','wb')
                            for data_chunk in r.iter_content(50000):
                                book.write(data_chunk)
                            book.close()
                        else:
                            print('run this script again to get your book for PG.')
                        
                        checker=1
                    elif answer.lower()=='n' or answer.lower()=='no':
                        print('Thank you for trying this downloader. It was a nice book, you should have downloaded :)')
                        checker=1
                    else:
                        print('Please give a vaild input.')

else:
    print('check your damn internet.')
