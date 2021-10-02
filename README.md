
# `Helpful resources and points:`

**`make your .py script a terminal command`**
- make script executable
```sh
chmod +x `name-of-script`
```
- add a shebang line(`#!bin/sh`) that points to system `Python` interpreter
```python
#-----add this line at the top of your script-----#
#!/usr/bin/env python 
#----- above is specific for python-------#
```
- create `~/bin` directory in user home directory
```sh
mkdir --parents ~/bin
# to avoid exisiting parent error flag it with `--parents`
```
- rename script and copy it into `~/bin` directory
```sh
mv script.py script
cp script ~/bin
```
- add `PATH` to the `.bash_profile` or `.profile` file
```sh
gedit .bash_profile
## add this line into `.bash_profile`
export PATH=$PATH":$HOME/bin" # this needs to be excat
```

---
**`jupyter server problem then might try to upgrade consol`**
```sh
pip install -U jupyter_console
```
---
**`some ideas to implement from automate-stuff-kitab`**
- Open all links on a page in separate browser tabs.
- Open the browser to the URL for your local weather.
- Open several social network sites that you regularly check.
---
**`links to learn basic html`**
- http://htmldog.com/guides/html/beginner/
- http://www.codecademy.com/tracks/web/
- https://developer.mozilla.org/en-US/learn/html/
---
**`hot to get free accuweather api`**

    Go to AccuWeather
    Register or log in
    Create new application at Application page

---
**`convert bs4.BeautifulSoup object(in json) into dictionry`**
```python
# convert into string
bs_obj_str=str(bs_ojecct)
# use json.loads() to parse valid json string into python dict
bs_dict=json.loads(bs_obj_str)
#####
# It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.
#####
```

**`radio-garden api links`**
```
#Get all country and cities

http://radio.garden/api/ara/content/places

(stations by city, gps coordinates)

#Get info of city and Stations by city (last id is id_city)

http://radio.garden/api/ara/content/page/W9g0lZfQ

#Get info of specific station (last id is id_station)

http://radio.garden/api/ara/content/channel/tMGsmGxF

#Example Stream URL (id is id_station)

http://radio.garden/api/ara/content/listen/tMGsmGxF/channel.mp3
```