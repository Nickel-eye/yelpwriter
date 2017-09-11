import random
import markovgen

restname='c-and-n-pizza-newton'

with open('%s_reviews.txt' %restname, 'r') as f:
	reviews = f.readlines()

with open('%s_reviews.txt' %restname, 'r') as f:
	ratings = f.readlines()

ratings = list(map(int, ratings))
indices = [i for i, x in enumerate(ratings) if x == 5]

rev = []
for i in indices:
	r = reviews[i].replace("[","")
	r = r.replace("]","")
	r = r.replace("'","")
	r = r.replace('"',"")
	r = r.replace(r'\n',"")
	rev.append(r)

str_ = "".join(rev[0:len(rev)])
print(str_)
print(type(str_))

markov = markovgen.Markov(rev)
print(markov.generate_markov_text(100))
