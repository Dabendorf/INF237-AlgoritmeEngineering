# https://uib.kattis.com/problems/tarifa

import sys
from typing import Tuple
from collections import defaultdict

def main():
	X = int(sys.stdin.readline())
	N = int(sys.stdin.readline())

	for i in range(N):
		# Reads one Integer per line
		line = int(sys.stdin.readline().strip())
		print(line)
		

if __name__ == "__main__":
	main()