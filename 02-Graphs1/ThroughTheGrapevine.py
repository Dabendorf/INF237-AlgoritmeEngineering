# https://uib.kattis.com/problems/grapevine

import sys
from typing import Tuple
from collections import defaultdict

""" Spread a rumor to as many people as possible.
	Every person has skepicism level.
	It's number of people from which they want to hear the rumor
	before spreading it themselves.

	One starting person spreads it to all people she knows (represented by graph)
	Every day the next people who did hear it the day before spread it
	Find out number of people who know the rumors

	Solution:
	- Generate adjacency list, skepticism dictionary and a dictionary
	  about who told who'm already
	- Make list of next spreaders containing only the starter
	- Make a loop with amount of days.
	- In each iteration, loop through next spreaders and get their neighbours.
	- Add their spreader to the told_list and check skepticism level. If it is reached, mark them as a next_round_spreader
	"""
def main():
	n, m, d = sys.stdin.readline().strip().split(" ")

	adj_list = defaultdict(lambda: list())
	skepticism_list = dict()
	told_list = defaultdict(lambda: set())

	# Read skepticism list
	for i in range(int(n)):
		# Reads one list of integers per line
		case_str = sys.stdin.readline().strip().split(" ")
		name, level = case_str
		skepticism_list[name] = int(level)

	for i in range(int(m)):
		# Reads one list of integers per line
		case_str = sys.stdin.readline().strip().split(" ")
		fra, til = case_str
		adj_list[fra].append(til)
		adj_list[til].append(fra)

	spreader = sys.stdin.readline().strip()
	
	"""print(f"Spreader: {spreader}")
	print(f"Adj_list: {adj_list}")
	print(f"skepticism_list: {skepticism_list}")
	print(f"Told_list: {told_list}")"""

	next_spreaders = [spreader]
	for i in range(int(d)):
		spreaders_after = list()
		for spr in next_spreaders:
			for to_tell in adj_list[spr]:
				told_list[to_tell].add(spr)
				if len(told_list[to_tell]) == skepticism_list[to_tell]:
					spreaders_after.append(to_tell)
		next_spreaders = spreaders_after
		#print(f"Told_list after day {i}: {told_list}")
	
	if spreader in told_list:
		print(len(told_list)-1)
	else:
		print(len(told_list))

if __name__ == "__main__":
	main()