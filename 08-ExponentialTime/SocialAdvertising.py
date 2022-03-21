import sys
import itertools
from functools import reduce

if len(sys.argv) > 1:
	debug = print
else:
	debug = lambda *_,**__:None

""" There are n people and each of them has a list of friends.
	We would like to post advertisements on their social media wall which all of their friends are going to see (including themselves)
	Find the minimum amount of people to post advertisement to such that all peopel are reached

	Solution:
	- After reading friend lists, one converts friend lists into binary strings (integers)
	- Person x is 2**(x-1), e.g. {1,4,5} is 1+8+16=25
	- If we have n people, we need to reach to number 2**n-1 by logical OR on an amount of subsets (represented by integer)
	- At first I prune duplicates (same friend lists) and go through pairs of them and remove numbers which are subsets of others
	- In the end, I loop through each size from 2 to n and try for each combination if they output 2**n-1 after logical or
	- If this is the case, the loop breaks and the minimum number is found
	"""
def main():
	num_of_cases = int(sys.stdin.readline())

	# Read every testcase
	for _ in range(num_of_cases):
		sets = []
		num_of_people = int(sys.stdin.readline())
		
		# Generate friendlists
		for person_idx in range(num_of_people):
			person_friends = set([int(i) for i in sys.stdin.readline().strip().split(" ")][1:])
			person_friends.add(person_idx+1)
			sets.append(person_friends)

		debug(sets)

		# Calculate numbers (binary strings) for friend lists
		numbers = set()
		for s in sets:
			num = 0
			for idx in range(num_of_people):
				if idx+1 in s:
					num += (2**(idx))
			numbers.add(num)
		
		debug(numbers)

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
				if found== True:
					break
				iterator = itertools.combinations(numbers, i)

				for next_subset in iterator:
					# Logical or over sets
					overall = reduce(lambda a, b: a|b, next_subset)
					
					# Check break condition
					if overall == number_searched:
						print(f"{i}")
						found = True
						break
			if not found:
				print(num_of_sets)

if __name__ == "__main__":
	main()