# << Swami Shreeji >>
# @nishantpatel ; 16 Oct 2017
# Algorithms --> Strings --> twoChars

import sys
import collections
from itertools import combinations
import string

testStrLen = raw_input()
testStr = raw_input()

testStrInfo = collections.Counter(testStr)
uniqueLetters = list(testStrInfo)

# TESTING
print uniqueLetters

# Get all pair combos
storeCombos = list()
for pair in combinations(uniqueLetters, 2):
	 pairedUp = pair[0] + pair[1]
	 storeCombos.append(pairedUp)

# Produce all possible strings of 2 unique letters from testStr
for elem in storeCombos:
	result = ''.join(c for c in testStr if c == (elem[0]) or c == (elem[1]))
	print result


	#potentialAns = testStr.strip(everything except pair[0] and pair[1])