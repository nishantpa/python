# << Swami Shreeji >>
# @nishantpatel ; 16 Oct 2017
# Algorithms --> Strings --> twoChars

import sys
import collections

# Take from stdin
testStrLen = raw_input()
testStr = raw_input()

testStrInfo = collections.Counter(testStr)
uniqueLetters = list(testStrInfo)

print uniqueLetters
print uniqueLetters[1]