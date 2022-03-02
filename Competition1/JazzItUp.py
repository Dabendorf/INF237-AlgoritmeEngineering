import sys
from typing import Tuple
from collections import defaultdict
from math import gcd

def main():
	n = int(sys.stdin.readline())
	gen = square(n+1)

	squares = list((gen))
	for m in range(2, n):
		product = m*n
		possible = True
		for s in squares:
			if product % s == 0:
				possible = False
				break

		if possible:
			print(m)
			exit(0)
		
		



def square(up_to):
	for x in range(2,up_to):
		yield x**2
		

if __name__ == "__main__":
	main()