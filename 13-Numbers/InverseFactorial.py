from sys import stdin
from math import log, ceil

# https://uib.kattis.com/problems/inversefactorial

""" For a number n!, find the original number n

	Solution:
	- Logarithm tricks
	- The length of a number n is floor(log10(n))
	- Also, log(a*b) = log(a)+log(b)
	- One only needs to sum up the length of every number until we get the same length as n
	- Extracases for 1-7 are needed, since factorials there have ambitious lengths
		
	"""
num = stdin.readline().strip()

len_orig = len(num)

len_new = 0

if len_orig <= 4:
	if int(num) == 1:
		print(1)
	elif int(num) == 2:
		print(2)
	elif int(num) == 6:
		print(3)
	elif int(num) == 24:
		print(4)
	elif int(num) == 120:
		print(5)
	elif int(num) == 720:
		print(6)
	elif int(num) == 5040:
		print(7)
else:
	for i in range(1, 1000001):
		len_new += log(i, 10)
		if len_orig == ceil(len_new):
			print(i)
			exit(0)