# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 21:16:00 2023

@author: HP
"""

import nltk
from nltk.stem import PorterStemmer

paragraph = """The Bill and Melinda Gates Foundation’s Robert Rosen will also participate in the event, where more than 100 representatives from global family offices will discuss asset and wealth management opportunities in the city. The government is planning to roll out a tax concession for single family offices among other policies on Friday, Hong Kong Secretary for Financial Services and Treasury Christopher Hui said during a Bloomberg Television interview on Tuesday. """

sentences = nltk.sent_tokenize(paragraph)
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    newwords = [stemmer.stem(word) for word in words]
    sentences[i] = ' '.join(newwords)
    
