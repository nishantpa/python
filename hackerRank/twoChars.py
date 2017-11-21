# << Swami Shreeji >>
# @nishantpatel ; 16 Oct 2017
# Algorithms --> Strings --> twoChars beabeefeab
# NOTE: Lost my place. Came back to this after months

import sys
import collections
from itertools import combinations
import string

testStrLen = raw_input()
testStr = raw_input()

# Extract unique chars
testStrInfo = collections.Counter(testStr)
uniqueLetters = list(testStrInfo)

# Get all pair combos
storeCombos = list()
for pair in combinations(uniqueLetters, 2):
	 pairedUp = pair[0] + pair[1]
	 storeCombos.append(pairedUp)

# Produce all possible strings of 2 unique letters from testStr
storePotentialStrings = list()
for elem in storeCombos:
	result = ''.join(c for c in testStr if c == (elem[0]) or c == (elem[1]))
	storePotentialStrings.append(result)

# Filter out nonalternating character strings
for elem in storePotentialStrings:
	i = 1
	temp = elem[0]
	char = elem[i]
	if char == temp:
		storePotentialStrings.remove(elem)
	for char in elem[1:]:
		if char == temp:
			storePotentialStrings.remove(elem)
			temp = char
		break
	

for elem in storePotentialStrings:
	print elem