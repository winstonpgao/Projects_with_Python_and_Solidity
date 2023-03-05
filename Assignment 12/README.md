# Sentiment Analysis


## This Readme file has the Following Sections:
1. Sentiment Analysis
2. Natural Language Processing
3. Named Entity Recognition


## Sentiment Analysis:
Usd the newsapi to pull the latest news articles for Bitcoin and Ethereum and create a DataFrame of sentiment scores for each coin.

Questions:
Q: Which coin had the highest mean positive score?

A: Ethereum (0.057) has the highest mean positive score vs. Bitcoin (0.027)

Q: Which coin had the highest compound score?

A: Bitcoin (0.9217) had the highest coumpound score vs. Ethereum (0.9001)

Q. Which coin had the highest positive score?

A: Bitcoin (0.353) had the highest positive sore vs. Ethereum (0.313)


## Natural Language Processing:

NLTK and Python are used to tokenize text, find n-gram counts, and create word clouds for both coins.

10 Top Words for Bitcoin:
 ('char', 90),
 ('bitcoin', 77),
 ('reuters', 71),
 ('currency', 34),
 ('taken', 32),
 ('photo', 30),
 ('virtual', 27),
 ('illustration', 25),
 ('seen', 24),
 ('reutersdado', 24)

![](/1.png)

10 Top Words for Ethereum:
 ('char', 92),
 ('bitcoin', 43),
 ('ethereum', 28),
 ('reuters', 25),
 ('cryptocurrency', 24),
 ('photo', 20),
 ('currency', 20),
 ('virtual', 19),
 ('ha', 19),
 ('taken', 18)
 
![](/2.png)

## Named Entity Recognition:

The named entity recognition model for both coins and visualize the tags using SpaCy.

![](/3.png)
