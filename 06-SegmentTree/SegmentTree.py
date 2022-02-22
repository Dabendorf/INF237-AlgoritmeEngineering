from re import I
import sys
from typing import Tuple
from collections import defaultdict

def main():
	data = [3, 5, 6, 2, 0, 9, 8, 1]

	tree = [0] * len(data) + data
	
	tree2 = fill(tree)

	print(tree2)

def fill(tree, op=sum):
	left = lambda i: 2 * i
	right = lambda i: 2 * i + 1

	internal = range(1, len(tree) // 2)
	for idx in reversed(internal): # internal nodes backwards
		tree[idx] = op((tree[left(idx)], tree[right(idx)]))

	return tree

def update(tree, idx, value, op=sum):
	left = lambda i: 2 * i
	right = lambda i: 2 * i + 1
	parent = lambda i: i // 2

	tree[idx] = value
	while (idx := parent(idx)) > 0:
		tree[idx] = op((tree[left(idx)], tree[right(idx)]))

def query_(T, l, r):
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
		

if __name__ == "__main__":
	main()