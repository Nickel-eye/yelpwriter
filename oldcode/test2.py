from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib
import re

page_url = "https://www.yelp.com/search?find_desc=s+and+i+thai&find_loc=Boston%2C+MA&ns=1"
soup = BeautifulSoup(urllib.request.urlopen(page_url).read(),"html5lib")
restnames = soup.findAll('a', class_="js-analytics-click")
for r in restnames:
	name = re.findall(r'href="/biz/(.*?)><span>',str(r))
	if name:
		restname = str(name)
		restname = restname.replace('"',"")
		restname = restname.replace("'","")
		restname = restname.replace("[","")
		restname = restname.replace("]","")
		break

print(restname)