#coding=utf-8

import re
import requests

target = 'https://movie.douban.com/cinema/nowplaying/beijing/'
source = requests.get(target).text

pattern = u'data-title="([\w\u4e00-\u9fa5]+)".*?data-score="([\w.]+)"'
films = re.findall(pattern, source, re.S)

# high score on top
films = sorted(films, key = lambda x: x[1], reverse = True)

print '%d films found.' % len(films)
for film in films:
    name = repr(film[0]).replace('u\'', '\'')
    name = name.decode('unicode-escape')
    print name, film[1]
