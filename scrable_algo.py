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


def scrabble_score(word):
	"""
	Function that outputs the score of a word (sum of the scores of each letter)
	
	Parameters
	----------
	word : string. (the word in question)
	
	Returns
	-------
	score_tot : int. (the score for the word)
	"""	
	
	total = []
	for letter in word:
		total.append(score[letter.lower()])
	score_tot = sum(total)
	return score_tot
	
#def extract_key_words(sentence, n = 3):
	# TO DO : Extract the n most relevant key words according to the score
	#         ? what about removing the stop words from nltk stopwords ?
	
				
print scrabble_score("Helix")
