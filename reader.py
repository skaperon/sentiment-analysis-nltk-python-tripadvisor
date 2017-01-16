import csv
import nltk
import re
from array import *
# Array Setting
punct = []
stops = []
ntitle = []
ncontent= []
collection = []
# ID Setting
_id = 0
with open('wordlist/punctuation.txt', 'r') as obj1:
	for s in obj1:
		punctuations = s.rstrip()
		punctuations = re.escape(punctuations)
		punctuations = re.compile(punctuations)
		punct.append(punctuations)
with open('wordlist/stopwords.txt', 'r') as obj2:
	for s in obj2:
		#Lowercase words and strip newlines ans whitespaces
		stopwords = s.lower().rstrip()
		stopwords = re.escape(stopwords)
		stopwords = re.compile("{}{}{}".format("\\b", stopwords, "\\b"))
		stops.append(stopwords)
#Open a csv to retrieve the reviews
with open('tripadvisor_dieburg.csv') as file:
	reader = csv.DictReader(file)
	#Get the title and content and replace the expressions
	#Starrating [review_stars] and ID's [_id]
	for row in reader:
		review_stars = row['review_stars'].split("von")[0]
		new_title = row['title'].lower()
		new_content = row['content'].lower()
		_id += 1
		#Regular Expression Handling
		for r in punct:
			# r = re.compile(r)
			new_title = re.sub(r, '', new_title)
			new_content = re.sub(r, '', new_content)
		for r in stops:
			#patter = "{}{}{}".format("\\b", r, "\\b")
			#r = re.compile(patter)
			new_title = re.sub(r, '', new_title)
			new_content = re.sub(r, '', new_content)
		#Nltk Tokenizer
		new_title = nltk.word_tokenize(new_title)
		new_content = nltk.word_tokenize(new_content)
		#Appending to the arrays
		ntitle.append(new_title)
		ncontent.append(new_content)
		collection.append(
		[
			_id,
			row['title'],
			row['content'],
			row['city'],
			row['hotel_name'],
			review_stars,
			row['helpful_reader']
		])
