from re import I
import sys
from typing import Tuple
from collections import defaultdict
from math import ceil, log2

def main():
	N, K, Q = list(map(int,sys.stdin.readline().strip().split()))

	real_length = pow(2, ceil(log2(N)/log2(2)))
	#data = [0] * real_length

	tree = [0] * 2*real_length
	
	#tree = fill(tree)

	#print(f"Start tree: {tree}")
	#print(f"Length tree: {len(tree)}")

	for line in sys.stdin:
		line_temp = line.strip().split()
		
		# Snow level change (L, R, D)
		if line_temp[0] == "!":
			L = int(line_temp[1])
			R = int(line_temp[2])
			D = int(line_temp[3])
			for i in range(L, R+1):
				tree = update(tree, real_length+i, D, op=sum)
			#print(f"Update {line_temp}: {tree}")
			#print(f"Heights: {tree[len(tree)//2:]}")
		# Snow level query (X)
		else:
			X = int(line_temp[1])
			#level = query(tree, X, X)
			level = tree[real_length+X]
			print(level)
	
	#tree2 = fill(tree)

	#print(tree2)

def fill(tree, op=sum):
	left = lambda i: 2 * i
	right = lambda i: 2 * i + 1

	internal = range(1, len(tree) // 2)
	for idx in reversed(internal): # internal nodes backwards
		tree[idx] = op((tree[left(idx)], tree[right(idx)]))

	return tree

def update(tree, idx, value, op=sum):
	#print(f"{idx} {value}")
	left = lambda i: 2 * i
	right = lambda i: 2 * i + 1
	parent = lambda i: i // 2

	tree[idx] += value
	idx = parent(idx)
	while idx > 0:
		#print(idx)
		tree[idx] = op((tree[left(idx)], tree[right(idx)]))
		idx = parent(idx)
	#print("====")
	return tree

"""def query_(T, l, r):
	left = lambda i: 2 * i
	right = lambda i: 2 * i + 1
	parent = lambda i: i // 2

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

def query(T, l, r, op=sum):
	return op(query_(T, l, r))"""

if __name__ == "__main__":
	main()