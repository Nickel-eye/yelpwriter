import crawler
import os.path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib
import re

namesrch = input("What's the restaurant name? ")
locsrch = input("What town is it near? (e.g. Boston MA) ")
print('\nSearching ...\n')

namewords = str.split(namesrch)
namesrch = "+".join(namewords)
locwords = str.split(locsrch)
locsrch = "+".join(locwords)

get_yelp_page = \
		lambda restname, page_num: \
			'http://www.yelp.com/biz/{0}' \
			'?start={1}'.format(restname, page_num)

get_yelp_search_page = \
		lambda namesrch, locsrch: \
			'http://www.yelp.com/search?find_desc={0}' \
			'&find_loc={1}'.format(namesrch, locsrch)

page_url = get_yelp_search_page(namesrch,locsrch)
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
		page_url = get_yelp_page(restname,0)
		soup = BeautifulSoup(urllib.request.urlopen(page_url).read(),"html5lib")
		rvcountraw = soup.findAll('div', itemprop="aggregateRating")
		for r in rvcountraw:
			rvcount = re.findall(r'"reviewCount">(.*?)</span>',str(r),re.DOTALL)
			rvcount = int(rvcount[0])
		for r in rvcountraw:
			nstars = re.findall(r'<meta content="(.*?)"',str(r),re.DOTALL)
			nstars = float(nstars[0])
		print('Found %s\n' %restname)
		print('%.1f-star average rating' %nstars)
		print('%d total reviews\n' %rvcount)
		yorno = input("Does this sound right?\n(y to continue, n to keep searching) ")
		if yorno == "y":
			break
		else:
			print("\n")
			continue

stars = int(input("How many stars would you like to give? "))
length = int(input("How many sentences do you want? "))

print('\n')

if os.path.isfile('./data/%s_ratings.txt' %restname):
	crawler.generate(restname,stars,length)
else:
	print('Collecting data ...')
	crawler.crawl(restname)
	crawler.generate(restname,stars,length)


