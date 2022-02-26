# https://uib.kattis.com/problems/moviecollection

import sys
from typing import Tuple
from collections import defaultdict
from math import ceil, log

""" There is a stack of movies with numbers 1 to n
	Each time we are interested in a movie, the programme outputs at which position from the top the movie is situated
	It then updates the positions of all movies

	Solution:
	- Implementation of a segment tree with a point update and a range query
	- The original leaf length is the number of movies + number of coming requests
	- Each leaf is either 0 or 1 depending if there is a movie there or not
	- There is a dictionary (list) telling at which leaf position every movie is situated
	- If a movie is requested, it sends a range query how many movies there are between its position and the top
	- It then updates at two positions, removing the movie at its old position, putting it into the new one
	"""
def main():
	num_of_cases = int(sys.stdin.readline())

	for _ in range(num_of_cases):
		num_of_movies, num_of_requests = list(map(int, sys.stdin.readline().strip().split(" ")))
		requests = list(map(int, sys.stdin.readline().strip().split(" ")))

		# Initialise tree
		total_leaf_length = num_of_movies + num_of_requests
		next_power_of_2 = pow(2, ceil(log(total_leaf_length)/log(2)));

		tree = ([0] * next_power_of_2) + ([1] * num_of_movies) + ([0] * (next_power_of_2-num_of_movies))
		
		# Fill tree
		fill(tree)

		# List with positions of each movie
		positions = [0]
		for k in range(1, num_of_movies+1):
			positions.append(num_of_movies-k)

		top_index = index(tree, num_of_movies)

		output_list = []
		# Loop for requests
		for req in requests:
			# For each request, calculate the number of movies between position and top
			pos_in_stack = query(tree, index(tree, positions[req]+1), top_index)
			output_list.append(str(pos_in_stack))

			# Remove the movie
			to_remove = index(tree, positions[req])

			# to add is the top_index, update information and positions
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

# The following functions are copied from Pål and describe a typical 
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