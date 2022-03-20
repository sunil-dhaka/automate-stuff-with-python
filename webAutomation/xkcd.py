# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
from bs4 import BeautifulSoup as bs
import os
from datetime import date

# %%
link='https://xkcd.com/'
r=requests.get(link)
print('Status from link, ',r.status_code)
soup=bs(r.text,features='html.parser')


# %%
total_posts=int(soup.select('a[accesskey="p"]')[0].get('href').strip('/'))+1
# added one for current page
# find it by using accesskey for previous page
checker=0
while(checker==0):
    print('There are total',total_posts,' comics on XKCD webpage.')
    start=int(input('What is your starting integer for requested post --> '))
    end=int(input('What is your ending integer for requested post --> '))
    if start <= end:
        checker=1
        os.makedirs('xkcd',exist_ok=True) # makes a home directory named 'xkcd' if does not exist
        post_link=list()
        post_title=list()
        post_title.append('Downloading comics from' +str(start)+' to '+str(end)+' on date ----'+(date.today()).strftime("%B %d, %Y"))
        requested_posts=end-start
        for i in range(requested_posts+1):
            curr_link='https://xkcd.com/'+str(i+start)
            r_page=requests.get(curr_link)
            if r_page.status_code!=200:
                print('bad request')
            else:
                curr_soup=bs(r_page.text,features='html.parser')
                finder=curr_soup.select('div[id="comic"] img')
                if len(finder)<1:
                    print('could not find comic on this page. Going to next comic page ...')
                else:
                    post_link.append('htpps:'+finder[0].get('src'))
                    post_title.append(str(i+start)+ ') '+finder[0].get('title')) 
                    # just to keep tab what particular comic was about and store it in .txt file
                    print('Downloading comic %s ...'%post_link[-1])
                    image_name=post_link[-1].split('/')[-1]
                    image=open(os.path.join('xkcd',image_name),'wb') # to store in xkcd folder created above
                    for image_chunk in r_page.iter_content(100000):
                        image.write(image_chunk)
                    image.close()
        post_title.append('Downloaded comics from '+str(start)+' to '+str(end)+' on date ----'+(date.today()).strftime("%B %d, %Y"))
        title_file=open(os.path.join('xkcd','titles.txt'), "a")
        for line in post_title:
            title_file.write(line+"\n")
        print('Downloading done.')

    else:
        print('------ please give a valid input ------')
