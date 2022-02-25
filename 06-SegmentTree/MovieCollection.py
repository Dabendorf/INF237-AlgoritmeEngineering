import sys
from typing import Tuple
from collections import defaultdict
from math import ceil, log

def main():
	num_of_cases = int(sys.stdin.readline())

	for _ in range(num_of_cases):
		num_of_movies, num_of_requests = list(map(int, sys.stdin.readline().strip().split(" ")))
		requests = list(map(int, sys.stdin.readline().strip().split(" ")))

		# Initialise tree
		total_leaf_length = num_of_movies + num_of_requests
		next_power_of_2 = pow(2, ceil(log(total_leaf_length)/log(2)));

		tree = ([0] * next_power_of_2) + ([1] * num_of_movies) + ([0] * (next_power_of_2-num_of_movies))
		
		fill(tree)

		print(tree)
		print(len(tree))
		positions = {k:(num_of_movies-k) for k in range(1, num_of_movies+1)}
		print(positions)

		top_index = index(tree, num_of_movies)
		print(top_index)
		print(tree[top_index])

		nr = 3

		print(f"Range: [{index(tree, positions[nr]+1)},{top_index})")
		print(f"Query: {query(tree, index(tree, positions[nr]+1), top_index)}")
		top_index += 1
		print("==========")


# Lambda functions copied from Påls slide
left = lambda i: 2 * i
right = lambda i: 2 * i + 1
parent = lambda i: i // 2
index = lambda T, i: len(T) // 2 + i

def fill(tree, op=sum):
	internal = range(1, len(tree) // 2)
	for idx in reversed(internal): # internal nodes backwards
		tree[idx] = op((tree[left(idx)], tree[right(idx)]))

def update(tree, idx, value, op=sum):
	tree[idx] = value
	while (idx := parent(idx)) > 0:
		tree[idx] = op((tree[left(idx)], tree[right(idx)]))

def query(T, l, r, op=sum):
	return op(query_(T, l, r))

def query_(T, l, r):
	yield T[l] # [l, r)
	while True:
		pl = parent(l)
		pr = parent(r)
		if pl == pr:
			return
		if l % 2 == 0:
			yield T[right(pl)]
		if r % 2 == 1:
			yield T[left(pr)]
		l,r = pl, pr

if __name__ == "__main__":
	main()