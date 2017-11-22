# << Swami Shreeji >>
# 21 Nov 2017
# Algo --> Implementation --> Encryption
# What's left? Pretty print it

import sys
import string
import math

# Cases
case0 = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots" # 54
case1 = "haveaniceday" # 12
case2 = "feedthedog" # 10
case3 = "chillout" # 8

def encrypt(args):
	# Step 1: Remove all whitespace
	args = args.replace(" ","")
	argsLen = len(args)

	# Prelim setup
	cols = 0
	rows = int (math.floor(math.sqrt(argsLen)))
	if rows * rows <= argsLen:
		cols = rows + 1

	print cols, rows
	# Define rect dimensions
	rect = [["" for x in range(rows)] for x in range(cols)]

	# Step 2: Build rect
	colNum = 0 ; rowNum = 0
	while True:
		for char in args:
			rect[colNum][rowNum] = char
			colNum += 1
			
			if colNum == cols:
				rowNum += 1
				colNum = 0
		print rect
		break
	

encrypt(case2)	
