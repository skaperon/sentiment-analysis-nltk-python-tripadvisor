# Sentiment Analysis on Tripadvisor with Python & NLTK
Export tripadvisor hotel data with scrapy, remove stopwords, tokenize with nltk and deploy algorithm. After this steps analyzed data will be stored into mongodb database. Then, you can see the result of analyzed tripadvisor reviews on our sentiment dashboard.

In this project we have the focus on german (Deutsch) language. We wanted to analyse the sentiments, emotions and feelings of reviewers about german hotels.<br>

At first you can get your needed raw data with python and scrapy framework from tripadvisor with this repository: <br>
https://github.com/monkeylearn/hotel-review-analysis

<hr>

We changed the spider request and did a item change. For a more specific request you must put this command into your terminal. <em>Example:</em>

<kbd>scrapy crawl tripadvisor_more -a start_url="https://www.tripadvisor.de/Hotels-g2049630-Dieburg_Hesse-Hotels.html" -o dieburger-hotels.csv </kbd>
<br>

Requirements:
- python package:   pymongo
- python package:   nltk
- database:         MongoDB
- python framework: Django


<br>
<img src="https://s29.postimg.org/j0rz7ch53/sentiment_analysis_projekt.jpg" />
<br>
This repository is in progress! If you want to collaborate, please send a <a href="mailto:uenvert90@googlemail.com">e-mail</a>. 
