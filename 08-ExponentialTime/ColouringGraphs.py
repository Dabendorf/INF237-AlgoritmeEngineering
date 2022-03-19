# https://open.kattis.com/problems/coloring

import sys
from collections import defaultdict
from itertools import product

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

	if is_bipartite(adj_list, [0]):
		print(2)
	else:
		"""first_neighbour_of_0 = list(adj_list[0])[0]
		num_of_cols = 3
		found = False
		while not found and not num_of_cols == 6:
			it = product(list(range(num_of_cols)), repeat=num_of_nodes-2)
			for iteration_temp in it:
				iteration = (0,) + iteration_temp[0:first_neighbour_of_0] + (1,) + iteration_temp[first_neighbour_of_0:]
				wrong = False
				for idx_node, col_node in enumerate(iteration):
					if wrong:
						break
					for neighbour in adj_list[idx_node]:
						if wrong:
							break
						if col_node == iteration[neighbour]:
							wrong = True

				if not wrong:
					#print(iteration)
					print(num_of_cols)
					exit(0)

			num_of_cols += 1"""

		# not found five colours solution
		c = colouring(adj_list, num_of_nodes)
		print(c)

def colouring(adj_list, num_of_nodes):
	result = [None] * num_of_nodes

	for node in range(num_of_nodes):
		assigned_neighbour_colours = set([result[i] for i in adj_list[node] if i is not None])

		# this fancy code doesnt work
		#colour = list(set(range(num_of_nodes)).difference(assigned_neighbour_colours)).sort()[0]
		#colour = sorted(list(set(range(num_of_nodes)).difference(assigned_neighbour_colours)))[0]
		#print(colour)

		# bad alternative
		colour = 0
		for assigned_col in assigned_neighbour_colours:
			if colour != assigned_col:
				break
			colour += 1
 
		result[node] = colour
 
	#print(result)
	#if None in result:
	#	return len(list(set(list(result))))-1
	return len(list(set(list(result))))


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