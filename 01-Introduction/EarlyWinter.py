# https://uib.kattis.com/problems/earlywinter

import sys
from typing import Tuple
from collections import defaultdict

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