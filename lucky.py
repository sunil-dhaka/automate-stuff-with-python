import requests,sys
from bs4 import BeautifulSoup as bs
import webbrowser

if len(sys.argv)>1:
    link='https://www.google.com/search?q='+' '.join(sys.argv[1:])
    print('Finding links for your search query ...')
    r=requests.get(link)
    soup=bs(r.text,features='html.parser')
    link_data=soup.select('a h3')
    links=list()
    total_links_found=len(link_data)
    for i in range(total_links_found):
        p_link=link_data[i].parent.get('href')
        if p_link!=None:
            links.append(p_link.split('&')[0].split('=')[1])
    print('\_/ all done. We have got ',total_links_found,'many links for your query on google.')
    no_of_links=int(input('how many links do you want to open -->'))
    no_of_links=min(no_of_links,total_links_found)
    print('Openeing pages in web-browser ...')
    for i in range(no_of_links):
        webbrowser.open(links[i])
    print('all links are open in your default browser.')
else:
    print('try it again with some query')