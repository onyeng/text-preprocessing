# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:38:31 2023

@author: HP
"""

import nltk


paragraph = """The Bill and Melinda Gates Foundation’s Robert Rosen will also participate in the event, where more than 100 representatives from global family offices will discuss asset and wealth management opportunities in the city. The government is planning to roll out a tax concession for single family offices among other policies on Friday, Hong Kong Secretary for Financial Services and Treasury Christopher Hui said during a Bloomberg Television interview on Tuesday. """

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

word_tags = []
for tw in tagged_words:
    word_tags.append(tw[0]+"_"+tw[1])
    
tagged_paragraph = ' '.join(word_tags)