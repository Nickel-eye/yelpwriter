restname = "blah"
reviewsList = ["blah"]
with open('./data/%s_reviews.txt' %restname, 'w') as f:
		for item in reviewsList:
			f.write("%s\n" % item)