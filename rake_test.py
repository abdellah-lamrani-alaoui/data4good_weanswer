# -*- coding: utf-8 -*-
"""
Created on Sat May 27 01:34:02 2017

@author: Abdellah
"""

# importing the libraries

import pandas as pd
import nltk
from rake_nltk import Rake
from tqdm import tqdm


data = pd.read_csv("questions-2017-05-23.csv")



# Method in order to get the n best keywords according to RAKE algorithm
def get_n_best_keywords(l, n = 3) :
	return [tuple_[1] for tuple_ in l[:n]]
	
dim = data.shape[0]
result = []

for i in tqdm(xrange(dim)):	
	r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters.
	r.extract_keywords_from_text(data.Content.iloc[i])
	list_keywords = r.get_ranked_phrases_with_scores()
	result.append(get_n_best_keywords(list_keywords))
	
data["extraction"] = result
	