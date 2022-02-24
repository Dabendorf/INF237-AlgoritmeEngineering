# https://uib.kattis.com/problems/uib.pointsofsnow

import sys
from typing import Tuple
from collections import defaultdict
from math import ceil, log2

""" We live in a one dimensional country and receive both weather reports telling about falling snow
	and queries how much snow there is at one place. Snow falls in the range [a,b) (badly described)
	Write a programme which stores these values and calculates the amount of snow at different places

	Solution:
	- Implementation of a segment tree with a range update and a point query
	- The query is the sum of the path of a node up to the trees root
	- The update goes to the leafs and works iteratively up to the parents depending if it is within the range or not
	"""
def main():
	N, K, Q = list(map(int,sys.stdin.readline().strip().split()))
	real_length = pow(2, ceil(log2(N)/log2(2)))

	tree = [0] * 2 * real_length

	for _ in range(K+Q):
		line_temp = sys.stdin.readline().strip().split()
		
		# Snow level change (L, R, D)
		if line_temp[0] == "!":
			L = int(line_temp[1])
			R = int(line_temp[2])
			D = int(line_temp[3])
			update(tree, index(tree, L), index(tree, R), D)

			# Debug stuff
			#print(tree)
			#print(f"Snow depths: {[query(tree, index(tree, i)) for i in range(0,N)]}")

		# Snow level query (X)
		else:
			X = int(line_temp[1])
			# Weird offset to the left
			level = query(tree, index(tree, X-1))
			print(level)

# Lambda functions copied from Påls slide
left = lambda i: 2 * i
right = lambda i: 2 * i + 1
parent = lambda i: i // 2
index = lambda T, i: len(T) // 2 + i

def update(tree, L, R, value):
	""" Takes as arguments a tree, a left boundary, a right boundary
		and the value of snow level change"""
	# Mark the left node
	tree[L] += value

	# Note: It looks like we must exclude the right place of the range to make it accepted in Kattis

	# Infinite loop for left and right
	while True:
		# Go up on both sides
		parent_left = parent(L)
		parent_right = parent(R)

		# If both paths merge, don't do anything more
		if parent_left == parent_right:
			return

		# If original node comes from left, mark the right one
		if L%2 == 0:
			right_child = right(parent_left)
			tree[right_child] += value

		# Omvendt
		if R%2 == 1:
			left_child = left(parent_right)
			tree[left_child] += value

		# Go one up
		L = parent_left
		R = parent_right
		

def query(tree, idx):
	""" Query on tree with idx """
	sum = 0

	# Sums up from idx up to root by tree traversing
	while idx != 0:
		#print(f"Query index: {idx}")
		sum += tree[idx]
		idx = parent(idx)

	return sum

if __name__ == "__main__":
	main()