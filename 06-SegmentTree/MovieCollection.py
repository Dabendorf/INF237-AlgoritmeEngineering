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

		#positions_old = {k:(num_of_movies-k) for k in range(1, num_of_movies+1)}
		positions = [0]
		for k in range(1, num_of_movies+1):
			positions.append(num_of_movies-k)

		#print(positions)
		#print(positions_old)
		#exit(0)

		top_index = index(tree, num_of_movies)

		output_list = []
		for req in requests:
			#print(f"Current tree: {tree}")
			#print(f"Range: [{index(tree, positions[req]+1)},{top_index})")
			#print(f"Query: {query(tree, index(tree, positions[req]+1), top_index)}")
			#print(f"To search for: {req}")
			#print(f"Dict: {positions}")
			pos_in_stack = query(tree, index(tree, positions[req]+1), top_index)
			output_list.append(str(pos_in_stack))
			to_remove = index(tree, positions[req])
			# to add is the top_index
			update(tree, to_remove, 0)
			update(tree, top_index, 1)
			positions[req] = top_index-next_power_of_2

			top_index += 1
		
		print(" ".join(output_list))


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
	
	while idx > 0:
		idx = parent(idx)
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