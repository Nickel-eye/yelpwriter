from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib
import argparse
import math
import re
import markovify
#import markovgen

def crawl(restname):
	get_yelp_page = \
		lambda restname, page_num: \
			'http://www.yelp.com/biz/{0}' \
			'?start={1}'.format(restname, page_num)

	page_url = get_yelp_page(restname,0)
	soup = BeautifulSoup(urllib.request.urlopen(page_url).read(),"html5lib")
	rvcountraw = soup.findAll('div', itemprop="aggregateRating")
	for r in rvcountraw:
		rvcount = re.findall(r'"reviewCount">(.*?)</span>',str(r),re.DOTALL)
	rvcount = int(rvcount[0])

	reviewsList=[]
	ratingsList=[]
	for page_num in range(0,rvcount,20):
		page_url = get_yelp_page(restname,page_num)
		soup = BeautifulSoup(urllib.request.urlopen(page_url).read(),"html5lib")

		reviews = soup.findAll('p', itemprop="description")
		ratings = soup.findAll('div', itemprop="reviewRating")

		for r in reviews:
			review = re.findall(r'>(.*?)<',str(r),re.DOTALL)
			reviewsList.append(review)

		for r in ratings:
			rating = re.findall(r'\d',str(r))
			ratingsList.append(rating[0])

		print('Page {a} of {b} done.'.format(a=int((page_num+20)/20), b=math.ceil(rvcount/20)))

	with open('./data/%s_reviews.txt' %restname, 'w') as f:
		for item in reviewsList:
			f.write("%s\n" % item)

	with open('./data/%s_ratings.txt' %restname, 'w') as f:
		for item in ratingsList:
			f.write("%s\n" % item)

def generate(restname,stars,length):

	with open('./data/%s_reviews.txt' %restname, 'r') as f:
		reviews = f.readlines()

	with open('./data/%s_ratings.txt' %restname, 'r') as f:
		ratings = f.readlines()

	ratings = list(map(int, ratings))
	indices = [i for i, x in enumerate(ratings) if x == stars]

	rev = []
	for i in indices:
		r = reviews[i].replace("[","")
		r = r.replace("]","")
		r = r.replace("'","")
		r = r.replace('"',"")
		r = r.replace(r'\n',"")
		rev.append(r)

	str_ = "".join(rev[0:len(rev)])

	text_model = markovify.Text(str_)
	print('\n')
	paragraph = []
	for i in range(length):
	    text = text_model.make_sentence()
	    if text != None:
	    	paragraph.append(text)
	paragraph = " ".join(paragraph)
	print(str(paragraph))


	# Print three randomly-generated sentences of no more than 140 characters
	#for i in range(3):
	 #   print(text_model.make_short_sentence(140))

	# markov = markovgen.Markov(rev)
	# gentext = markov.generate_markov_text(length)
	# print(gentext)
	# return gentext




