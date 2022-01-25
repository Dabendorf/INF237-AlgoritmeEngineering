# https://uib.kattis.com/problems/tarifa

import sys
from typing import Tuple
from collections import defaultdict

""" X gigabytes to spent per months, N months
	the following months are quantity of data spent
	Solution: Multiply (N+1)*X and substract every monthly value """
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