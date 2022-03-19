# https://open.kattis.com/problems/coloring

import sys
from collections import defaultdict
import math
import heapq
from itertools import combinations_with_replacement

""" Problem

	Solution:
	- 
	"""
def main():
	num_of_nodes = int(sys.stdin.readline())

	adj_list = defaultdict(lambda: set())
	for i in range(num_of_nodes):
		neighbours = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		
		for n in neighbours:
			adj_list[i].add(n)
			adj_list[n].add(i)

	print(adj_list)
	if is_bipartite(adj_list, [0]):
		print(2)
	else:
		num_of_cols = 3
		found = False
		while not found:
			it = combinations_with_replacement(list(range(num_of_cols)), num_of_nodes)
			for iteration in it:
				wrong = False
				for idx, node_col in enumerate(iteration):
					if wrong:
						break
					for neighbour in adj_list[idx]:
						if wrong:
							break
						if node_col == neighbour:
							wrong = True
				
				if not wrong:
					found = True
					print(iteration)
					print(num_of_cols)
					exit(0)

			num_of_cols += 1

def is_bipartite(adj_list, components):
	""" Checks if graph is bipartite by giving it colours"""
	# Colours are just True and False
	colours = dict()

	# List of components are different not connected components derived via the BFS function
	for c in components:
		queue = [c]
		colours[c] = True

		while queue:
			el = queue.pop()

			# Go through neighbours of a node
			for neighbour in adj_list[el]:
				# If has colour, check if its the same as origin, then graph is not bipartite
				if neighbour in colours:
					if colours[el] == colours[neighbour]:
						return False
				else:
					# If not, append it to queue and give it opposite colour
					queue.append(neighbour)
					colours[neighbour] = not colours[el]
	return True

		

if __name__ == "__main__":
	main()