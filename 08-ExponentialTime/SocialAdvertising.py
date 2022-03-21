import sys
from typing import Tuple
from collections import defaultdict
import itertools

""" Problem

	Solution:
	- 
	"""
def main():
	num_of_cases = int(sys.stdin.readline())

	# Read every testcase
	for _ in range(num_of_cases):
		sets = [set()]
		num_of_people = int(sys.stdin.readline())
		
		# Generate friendlists
		for person_idx in range(num_of_people):
			person_friends = set([int(i) for i in sys.stdin.readline().strip().split(" ")][1:])
			person_friends.add(person_idx+1)
			sets.append(person_friends)

		# Calculate numbers (binary strings) for friend lists
		numbers = set()
		for s in sets:
			num = 0
			for idx in range(num_of_people):
				if idx+1 in s:
					num += (2**(idx))
			numbers.add(num)

		# Remove sets included in other sets
		to_remove = set()
		for idx_a, a in enumerate(numbers):
			for idx_b, b in enumerate(numbers):
				if idx_a != idx_b:
					if a&b == a:
						to_remove.add(a)
					elif a&b == b:
						to_remove.add(b)
		numbers = numbers.difference(to_remove)

		num_of_sets = len(numbers)
		# Calculate number to aim for
		number_searched = 2**(num_of_people)-1

		# Iterate through all set combinations from size 1 to num_of_sets
		# Terminate if found or iterations over
		if number_searched in numbers:
			print(1)
		else:
			found = False
			for i in range(2, num_of_sets):
				iterator = itertools.combinations(numbers, i)
				next_subset = next(iterator)

				# Logical or over sets
				overall = 0
				for el in next_subset:
					overall |= el
				
				# Check break condition
				if overall == number_searched:
					print(i)
					found = True
					break
			if not found:
				print(num_of_sets)

if __name__ == "__main__":
	main()