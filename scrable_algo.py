# -*- coding: utf-8 -*-
"""
Created on Sat May 20 23:39:03 2017

@author: Abdellah
"""


# Defining the scores for each letter

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}


def scrabble_score(word, score):
	"""
	Function that outputs the score of a word (sum of the scores of each letter).
	
	Parameters
	----------
	word  : string. The word in question.
	score : dic. The dictionnary that contains the score per letter. 
	
	Returns
	-------
	score_tot : int. The score for the word.
	"""	
	
	total = []
	for letter in word:
		# Checking if the letter is taken into account for the scrabble score
		if letter.lower() in score.keys():
			total.append(score[letter.lower()])
	score_tot = sum(total)
	return score_tot
	
def extract_key_words(sentence, score_function, n , *args):
	""" 
	Function that extracts the most relevant key words according to the scrabble_score.
	
	Parameters
	----------
	sentence       : string. In our case the question from which we want to extract the key words.
	score_function : function. Function that computes the score fiven a word.
	*args          : arguments of the function. 
	n              : int. The number of keywords we want to extract (descending order).
	
	Returns
	-------
	keywords : list of strings. The list of the n most relevant kewords according the the score.
	"""
	
	words = sentence.split(" ")
	scores_words = {}
	for word in words :
		scores_words[word] = score_function(word, *args)
	keywords = sorted(scores_words, key = scores_words.get)[-n - 1 :][-1:0:-1]
	return keywords
	
	
# importing the key words
from nltk.corpus import stopwords

	
def extract_key_words_stowords(sentence):
	
	# To do : still needs to preprocess according to the punctuation
	
	"""
	Returns all the words that are not stop words.
	
	Parameters
	----------
	sentence : string. The sentence from which we want to extract the keywords.
	
	Returns
	-------
	keywords : list of strings. The list of the non stop words.
	"""	
	
	stop = set(stopwords.words("english"))
	keywords = [word.lower() for word in sentence.split(" ") if word.lower() not in stop]
	
	return keywords
	

# TO DO : Do the intersection between the two extraction methods

import unittest 

import unittest

class TestFunctions(unittest.TestCase):

	def test_scrabble_score(self):
		self.assertEqual(scrabble_score("abdel", score), 8)
		self.assertEqual(scrabble_score("ABDel", score), 8)
		self.assertEqual(scrabble_score("ABD12 el", score), 8)
		self.assertEqual(scrabble_score("test", score), 4)
		self.assertEqual(scrabble_score("we", score), 5)
		self.assertEqual(scrabble_score("answer", score), 9)
		self.assertEqual(scrabble_score("aa", score), 2)
		
	def test_extract_key_words(self):
		self.assertEqual(extract_key_words("we answer test aa", scrabble_score, 3, score), ["answer", "we", "test"])
		self.assertEqual(extract_key_words("we answer test aa", scrabble_score, 2, score), ["answer", "we"])
	
	def test_extract_key_words_stowords(self):
		self.assertEqual(extract_key_words_stowords("What are these questions"), ["questions"])
if __name__ == '__main__':
    unittest.main()
				


