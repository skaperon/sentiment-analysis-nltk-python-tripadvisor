# Sentiment Aanalysis on Tripadvisor with Python & NLTK
Export tripadvisor hotel data to mongodb with scrapy, 
remove stopwords, tokenize reviews with nltk and segmenting reviews for a sentiment analysis process and dashboard.

In this project we have the focus on german (Deutsch) language. We want to analyse the sentimentals of hotel reviews in Germany.<br>

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
[![pdf.jpg](https://s29.postimg.org/j0rz7ch53/sentiment_analysis_projekt.jpg)](https://postimg.org/image/f4enbcw5f/)
<br>
This repository is in progress! If you want to collaborate, please send a <a href="mailto:uenvert90@googlemail.com">e-mail</a>. 
