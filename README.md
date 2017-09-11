# yelpwriter
Yelp review generator, lets you search for a restaurant and input the desired star rating and number of sentences, and uses a Markov model to generate a new review.

This was a fun project I did while still fresh to Python as a foray into NLP. The crawling is slow as I used BeautifulSoup, but this is not intended to be a scalable crawler, especially as crawling Yelp is looked down upon (see Yelp's robots.txt).

## Project Explanation

_yelp.py_: This is the main executable file. Lets you search for the restaurant and location, and input the desired star rating and length of review (in sentences). Reviews and ratings data is saved, unless it has already been downloaded for the particular restaurant, in which case the download is skipped.

_crawler.py_: Defines the main functions for crawling the Yelp site and saving the data, as well as for generating Markov chain models for creating new text. I used the _markovify_ package for the models and text generation.

## Future Directions
I am exploring building a Recurrent Neural Network with Keras for the language generation. Possibly I can use a pre-trained RNN and do transfer learning to match the style/tone of a particular number of stars review for each particular restaurant.
