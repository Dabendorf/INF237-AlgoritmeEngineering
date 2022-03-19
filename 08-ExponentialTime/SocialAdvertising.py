import sys
from typing import Tuple
from collections import defaultdict

""" Problem

	Solution:
	- 
	"""
def main():
	num_of_cases = int(sys.stdin.readline())

	for _ in range(num_of_cases):
		sets = list(set())
		num_of_people = int(sys.stdin.readline())
		for person_idx in range(num_of_people):
			person_friends = set([int(i) for i in sys.stdin.readline().strip().split(" ")][1:])
			person_friends.add(person_idx+1)
			sets.append(person_friends)
		print(sets)
		

if __name__ == "__main__":
	main()