#

import re   # regular expression
import requests

#url = 'http://www.baidu.com'
#url = 'https://search.jd.com/Search?keyword=shell&enc=utf-8&wq=shell&pvid=74ab31bb5135476389e063debe4458c4'
#url = 'http://search.yhd.com/c0-0-1004212/'
url = 'https://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_18374&sort=sort_rank_asc&trans=1&JL=3_%E5%93%81%E7%89%8C_%E5%B0%8F%E7%B1%B3%EF%BC%88MI%EF%BC%89#J_crumbsBar'
html = requests.get(url).text

#pattern = '<img.*?src="(.*?)" />'
#pattern = '<img[\w ="/.-]+src="'
#pattern = '<img[\w ="/.-]+src="([\w\/.]+)" />'
#pattern = 'class="promo-words"'
#pattern = '<img alt="" src="([\w/.]+)">'
pattern = 'data-lazy-img="([\w/.]+)">'

pic_url = re.findall(pattern, html)

print '%d image url found' % len(pic_url)
i = 0
for each in pic_url:
    print each
    pic = requests.get('http:' + each)

    fp = open('./mi/' + str(i) + '.jpg', 'wb')
    fp.write(pic.content)
    fp.close()

    i += 1
