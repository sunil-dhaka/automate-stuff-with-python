from helium import *

url='https://www.youtube.com/c/JohnWatsonRooney/videos?view=0&sort=da&flow=grid'

start_chrome(headless=False)
go_to(url)
#=======
# here I am trying to rexh to the bottom
# but still getting only 30 videos
#=======
scroll_down(num_pixels=5000)
press(PAGE_DOWN)
Config.implicit_wait_secs=10
videos=find_all(S('#video-title'))
# don't forget to use web_element
# docs: https://selenium-python-helium.readthedocs.io/en/latest/api.html#
titles=[item.web_element.text for item in videos]
print('total videos:',len(titles))
print(f'first video is {titles[0]}')
kill_browser()