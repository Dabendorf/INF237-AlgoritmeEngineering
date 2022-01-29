# https://open.kattis.com/problems/tiredterry

import sys
from typing import Tuple
from collections import defaultdict

""" Terry has a sleep pattern of size n (repeating) consisting of seconds
	of sleep (Z) or awakeness (W). Given a period of seconds p, how many seconds i
	are there for which intervals [i-p+1, i] he was sleeping for less than d seconds?
	
	Solution:
	Append the list of letters by the length of p-1 and make a sliding window of size p over it
	Then count the appearences, compare it to d and count how often its less than d

	The pythonic way of fancy slicing does not get accepted due to horrible runtime
	This solution counts number of Z in first window and then
	just removes the first and adds the next letter to the z-counter
	"""
def main():
	n, p, d = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	sleep_string = list(sys.stdin.readline().strip())
	sleep = sleep_string + sleep_string[0:p]

	counter = 0
	amount_z = sleep[0:0+p].count("Z")
	pointer_start = 0
	pointer_next = p

	for i in range(len(sleep_string)):
		if amount_z < d:
			counter += 1
		if sleep[pointer_start] == "Z":
			amount_z -= 1
		if sleep[pointer_next] == "Z":
			amount_z += 1
		pointer_start += 1
		pointer_next += 1

	print(counter)
	
	""" Version 1: Python Slicing stuff, time limit exceeded
	counter = 0
	for i in range(len(sleep_string)):
		if sleep[i:i+p].count("Z") < d:
			counter += 1

	print(counter)"""

if __name__ == "__main__":
	main()