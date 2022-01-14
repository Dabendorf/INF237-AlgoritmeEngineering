# https://uib.kattis.com/problems/tarifa

import sys
from typing import Tuple
from collections import defaultdict

def main():
	X = int(sys.stdin.readline())
	N = int(sys.stdin.readline())

	sum = (N+1)*X
	for i in range(N):
		# Reads one Integer per line
		line = int(sys.stdin.readline().strip())
		sum -= line
	
	print(sum)
		

if __name__ == "__main__":
	main()