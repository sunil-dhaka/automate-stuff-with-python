from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from PyInquirer import prompt
import time


query=input('Which radio station today ')
radio=webdriver.Firefox() # with Chrome also gives excat same result
radio.get('https://radio.garden')
print('window is running in background :)')
time.sleep(2)
explore_favorites_search_settings=radio.find_elements_by_class_name('Tab_container__3GACT')
search=explore_favorites_search_settings[2]
if search.text=='Search':
    #then only go ahead
    # first click search
    search.click()
    #then give it the query search-input gotten from user
    search_input=radio.find_element_by_id('search-input')
    #to make sure it is clear
    search_input.clear()
    # git it query
    search_input.send_keys(query)
    time.sleep(5)
    # now we have some results and other wise not some results
    names=radio.find_elements_by_class_name('ListItem_titleContainer__W5lqX')
    links=radio.find_elements_by_class_name('ListItem_linkContainer__32x8m')
    if len(names)>1:
        total_radio_channels=len(names)-1 # to minus the svg-icon element
        print('we have found ',total_radio_channels,' for your query.')
        # get their names
        names_text_link=list() # to attach it with click links to play radio
        for i in range(total_radio_channels):
            names_text_link.append(str(i+1)+')'+'@ '.join(names[i+1].text.split('\n')))
            # no list needed as can run down a key-list store loop
            # and then rather then linking it with a string number :: why not just give the corresponding link element to it 
            #str(i+1) # this gets links[int(names_text_link[choosen])].click() -- boom blast

        prompt_list=list()
        for name in names_text_link:
            prompt_list.append(name)

        # now prompt this list
        which_book=[
                {
                    'type':'list',
                    'name':'type',
                    'message':'please choose a radio:',
                    'choices':prompt_list,
                    'default':0
                }
            ]
        answer=prompt(which_book)
        # prompt done and answer is also there
        # just click it
        number=int(answer['type'].split(')')[0])
        try:
            links[number].click()
            # no benefit of these not so good clicks
            '''radio.find_element_by_class_name('Control_modPlay__2uUh2').click()#pause
            radio.find_element_by_class_name('Control_modPlay__2uUh2').click()#play
            radio.find_element_by_class_name('Control_control__1ympy').click()#next'''
        except Exception as e:
            print(e)
            radio.close()

        #### work to do ####
        # click is not being carried more than 1 min
        # what could be the reason
        # what is the solution of the problem
        # don't why there is only onw radio clip is there for all radios I am not clicking stuff correctly
    else:
        print('we found no results')
        radio.close()
        print('closed window')
else:
    print("we did not find your radio's search box")
    radio.close()
    print('closed window')