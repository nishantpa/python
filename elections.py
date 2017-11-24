# << Swami Shreeji >>
# @nishantpatel ; 23 Nov 2017
# TASK:
# 	Get the candidate with the most votes. DONE
# 	Get the votes of all candidates who ran for president and vp PENDING

import csv
import sys
from collections import defaultdict

# Read once, power away after
def preWork():
	# Holds OFFICE, CANDIDATE and VOTES. Dups exist
	data = []
	with open('2016_general.csv') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	        candAndVotes = [row['OFFICE'], row['CANDIDATE'], int (row['VOTES'])] 
	        data.append(candAndVotes)
	return data


def mostVoted(args):
	result = defaultdict(int)
	for item in args:
		office, cand, votes = item
		result[(cand)] += votes

	# print dict(result)
	mostVotedCand = max(result, key=result.get)
	print mostVotedCand


def pAndVPVotes():
	print "Hello world"


csvData = preWork()
mostVoted(csvData)
pAndVPVotes()
