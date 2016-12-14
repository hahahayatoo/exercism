#!/usr/bin/python3 -V
# -*- coding: utf-8 -*-

def detect_anagrams(keyword, word_list):
	ans = []
	for word in word_list:
		if len(keyword) == len(word)\
		 and keyword.lower() != word.lower()\
		 and sorted(keyword.lower()) == sorted(word.lower()):
			ans.append(word)
	return ans
