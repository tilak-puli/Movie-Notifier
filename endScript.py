import os
import time

exception_string = "Trying to Install required module: "
try:
    import requests
except ImportError:
    print(exception_string + "requests\n")
    os.system('python -m pip install requests')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print(exception_string + "BeautifulSoup\n")
    os.system('python -m pip install beautifulsoup4')

try:
    from pygame import mixer
except ImportError:
    print(exception_string + "pygame\n")
    os.system('python -m pip install pygame')

import requests
from bs4 import BeautifulSoup
import re
import configparser

def getName(href):
    return href.split('/')[3].split('-movie')[0].replace('-', ' ')

def getMovieDetails(soup):
    a = soup.find('a', href=True)
    return {'href': a['href'], 'name': getName(a['href']), 'html': a}

def getThatreDetails(soup):
    a = soup.find('a', href=True)
    return {'href': a['href'], 'name': a.text, 'html': a}

def playSound():
    mixer.init()
    sound = mixer.Sound('dingdong.wav')
    sound.play()
    time.sleep(5)

config = configparser.ConfigParser()
config.read('params.ini')
website = 'https://paytm.com/movies/' + config['parameters']['city']
dates = config['parameters']['dates'].split(',')
movie_name = config['parameters']['movie'].lower()
theatre_name = config['parameters']['theatre'].lower()
theatre_class = config['parameters']['theatre_class']
count = int(config['parameters']['count'])
page = requests.get(website)
soup = BeautifulSoup(page.text, 'html.parser')
soup = soup.find_all("div", {"class": re.compile("MobileRunningMovie_runningMovie__.*")})
movies_list = list(map(getMovieDetails, soup))
res = None

for movie in movies_list:
    if movie_name in str(movie['name']).lower():
        res = movie
        break
if res is None:
    print('Movie not available')
    print('Found these movies')
    print(list(map(lambda x: x['name'], movies_list)))
# os._exit(1)

while True:
    if res is not None:
        for date in dates:
            res1 = 'https://paytm.com' + res['href'] + '?fromdate=' + date
            page2 = requests.get(res1)
            soup2 = BeautifulSoup(page2.text, 'html.parser')
            showtime_list = soup2.find_all('div', class_=theatre_class)
            showtime_list = list(map(getThatreDetails, showtime_list))

            found_theatre = None
            for theatre in showtime_list:
                if re.match(theatre_name, theatre['name'], re.IGNORECASE) is not None:
                    print('Success')
                    found_theatre = theatre
                    playSound()
                    break
            # os._exit(0)

            if found_theatre is None:
                print('movie is not available in theatre: ' + theatre_name)

                if len(showtime_list) >= count:
                    print('but movie is available in more than ' + str(count) + ' theatres')
                    playSound()

                print('Found theatres:')
                print(list(map(lambda x: x['name'], showtime_list)))

    time.sleep(60)
    # Please don't decrease this, we don't want to bring down paytm
# os._exit(1)
