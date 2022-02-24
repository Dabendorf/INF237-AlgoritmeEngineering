import sys
from typing import Tuple
from collections import defaultdict
from math import ceil, log2

def main():
	N, K, Q = list(map(int,sys.stdin.readline().strip().split()))

	real_length = pow(2, ceil(log2(N)/log2(2)))

	tree = [0] * 2*real_length
	maxHeight = height(real_length)

	for _ in range(K+Q):
		line_temp = sys.stdin.readline().strip().split()
		
		# Snow level change (L, R, D)
		if line_temp[0] == "!":
			L = int(line_temp[1])
			R = int(line_temp[2])
			D = int(line_temp[3])
			tree, val = update(tree, real_length+L, real_length+R, maxHeight, D, op=sum)
			#print(val)
			#print(tree)
			#print([query(tree,real_length+i) for i in range(0,N)])

		# Snow level query (X)
		else:
			X = int(line_temp[1])
			level = query(tree, real_length+X)
			print(level)

# Lambda functions
left = lambda i: 2 * i
right = lambda i: 2 * i + 1
parent = lambda i: i // 2
height = lambda i: int(log2(i))

# Calculates the range of leafs a node is representing
leaf_range_left = lambda i, maxHeight: 2**((maxHeight-height(i)))*i
leaf_range_right = lambda i, maxHeight: 2**((maxHeight-height(i)))*(i+1)-1

def update(tree, L, R, maxHeight, value, op=sum):
	""" Takes as arguments a tree, a left boundary, a right boundary, the max height,
		and the value of snow level change"""
	#print(f"NEW VALUE {value}")
	list_val = []

	# Temporary left boundary value
	l_temp = L
	
	# Infinite loop until a break condition happens
	while True:
		# Calculate parent of current left border
		parent_l_temp = parent(l_temp)

		# If that parent is the root, set value to root value and return
		if parent_l_temp == 0:
			tree[1] += value
			return tree, list_val

		# Else: Get leaf boundaries of that parent
		bound_l = leaf_range_left(parent_l_temp, maxHeight)
		bound_r = leaf_range_right(parent_l_temp, maxHeight)

		# If left boundary is to the left of L
		# then increase value of current node
		if bound_l < L:
			tree[l_temp] += value
			list_val.append(l_temp)

			# Update current left boundary to (right leaf boundary of parent node)+1
			l_temp = bound_r + 1

			# if that is larger than R, return tree
			if l_temp > R:
				return tree, list_val
		# if calculated boundary to the right bigger than R
		# then increase value of current node 
		elif bound_r > R:
			tree[l_temp] += value
			list_val.append(l_temp)

			# Update current left boundary to (right leaf boundary of origin node)+1
			l_temp = leaf_range_right(l_temp, maxHeight)+1

			# if that is larger than R, return tree
			if l_temp > R:
				return tree, list_val
		else:
			# if neither of this happens, go one node up to the parent
			l_temp = parent_l_temp

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