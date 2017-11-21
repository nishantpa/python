# << Swami Shreeji >>
# @nishantpatel ; 21 Nov 2017
# Google's Tech Dev Guide - Former Coding Interview Question
	# Compression and Decompression

# Test Cases & output:
# 3[abc]4[ab]c		--> abcabcabcababababc
# 2[3[a]b]			--> aaabaaab

import sys
import string

# Test cases | Interpretted as a tuple
case1 = "3[abc]4[ab]c"
case2 = "2[3[a]b]"

def decompress(args):
	# General Case
	currString = ""
	repeater = 0
	for char in args:
		if char.isdigit():
			repeater = int(char)
		if char.isalpha():
			currString = currString + char
		elif char == "]":
			for i in range(0, repeater):
				sys.stdout.write(currString)
			currString = "" 
		sys.stdout.write(currString)


decompress(case2)
print ""