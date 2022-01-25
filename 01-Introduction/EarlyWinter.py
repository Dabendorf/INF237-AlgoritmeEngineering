# https://uib.kattis.com/problems/earlywinter

import sys
from typing import Tuple
from collections import defaultdict

""" n years historical weather data and
	information d_i for every year about number of days between summer and snow
	Find out number of consecutive years before this one with larger summer-snow gap
	
	Solution: Enumerate through yearly data
	If number of that year larger than this year, increase counter
	If not, break up and return number of years
	If counter is still zero, then it never snowed that early"""
def main():
	first_line = sys.stdin.readline().strip().split(" ")
	n, d = int(first_line[0]), int(first_line[1])

	case_str = sys.stdin.readline().strip().split(" ")
	case = [int(i) for i in case_str]
	
	counter = 0
	found = False
	for ind, num in enumerate(case):
		if num > d:
			counter += 1
		else:
			found = True
			break
		#print(ind)
	if found:
		print(f"It hadn't snowed this early in {counter} years!")
	else:
		print("It had never snowed this early!")
		

if __name__ == "__main__":
	main()