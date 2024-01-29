# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:05:26 2023

@author: HP
"""

import nltk

paragraph = "The Candi Borobudur was built by Emperor Samaratungga"

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

namedEnt = nltk.ne_chunk(tagged_words)
namedEnt.draw()
