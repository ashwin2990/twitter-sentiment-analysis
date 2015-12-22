# example of program that calculates the number of tweets cleaned
import json
import unicodedata
import sys
import re
import csv
import nltk
#from nltk.corpus import stopwords
#stopset = list(set(stopwords.words('english')))

'''
Function name: read_tweets
Input: filename - filename to fetch the tweets
Description: This function reads in the json files and returns the twitter feeds. It reads the file line by
			line storing all the tweets in the tweet_feed array
Return type: tweet_feed - tweetcontaining all the tweets
'''
def read_tweets(filemame):
	tweet_feed=[]
	with open(filemame) as tweet_input:
		for line in tweet_input:
			if(len(line.split())>1):
				tweet_feed.append(json.loads(line))
	return tweet_feed



def clean_feed(tweet_feed):
	remove_url=re.sub(r"http\S+", "", tweet_feed)
	remove_retweet=re.sub(r"@\S+", "", remove_url)
	remove_punctuation=re.sub(r'[?|!|.|#]', "", remove_retweet)
	words_filtered = [e.lower() for e in remove_punctuation.split() if len(e) >= 3]

	return dict([(word, True) for word in words_filtered])# if word not in stopset])cleaned_feed

def rows_amount(filename):
    with open(filename) as f:
        for i, line in enumerate(f, 1):
            pass
    return i


def NaiveBayes(train_set,test_set):
	NBclassifier = nltk.NaiveBayesClassifier.train(train_set)
	print 'accuracy:', nltk.classify.util.accuracy(NBclassifier, test_set)

def MaxEnt(train_set,test_set):
	MaxEntClassifier = nltk.classify.maxent.MaxentClassifier.train(train_set, 'GIS', trace=3, encoding=None, labels=None,  gaussian_prior_sigma=0, max_iter = 10)
	print 'accuracy:', nltk.classify.util.accuracy(MaxEntClassifier, test_set)	

def main():
	row_count = rows_amount('Sentiment Analysis Dataset.csv')
	print row_count
	f = open('Sentiment Analysis Dataset.csv', 'rb')
	csv_f = csv.reader(f)
	total_set=[(clean_feed(row[3]),row[1]) for row in csv_f]
	train_set=total_set[1:int(0.75*row_count)]
	test_set=total_set[int(0.75*row_count)+1:]
	NaiveBayes(train_set,test_set)
	MaxEnt(train_set,test_set)


main()
