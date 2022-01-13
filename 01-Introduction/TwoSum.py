# https://uib.kattis.com/problems/twosum

import sys
from typing import Tuple
from collections import defaultdict

def main():
	case_str = sys.stdin.readline().strip().split(" ")
	case = [int(i) for i in case_str]

	print(case[0]+case[1])
		

if __name__ == "__main__":
	main()