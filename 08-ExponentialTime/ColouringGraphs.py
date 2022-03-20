# https://open.kattis.com/problems/coloring

import sys
from collections import defaultdict
#from itertools import product

""" Problem

	Solution:
	- 
	"""
def main():
	num_of_nodes = int(sys.stdin.readline())

	adj_list = defaultdict(lambda: set())
	for idx in range(num_of_nodes):
		neighbours = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		
		for n in neighbours:
			adj_list[idx].add(n)
			adj_list[n].add(idx)

	for key, val in adj_list.items():
		adj_list[key] = list(val)

	c = colouring(adj_list, num_of_nodes)
	print(c)

def colouring(adj_list, num_of_nodes):
	result = [-1] * num_of_nodes
 
	# Assign the first color to first vertex
	result[0] = 0
 
 
	# A temporary array to store the available colors.
	# True value of available[cr] would mean that the
	# color cr is assigned to one of its adjacent vertices
	available = [False] * num_of_nodes
 
	# Assign colors to remaining V-1 vertices
	for u in range(1, num_of_nodes):
		 
		# Process all adjacent vertices and
		# flag their colors as unavailable
		for i in adj_list[u]:
			if (result[i] != -1):
				available[result[i]] = True
 
		# Find the first available color
		cr = 0
		while cr < num_of_nodes:
			if (available[cr] == False):
				break
			 
			cr += 1
			 
		# Assign the found color
		result[u] = cr
 
		# Reset the values back to false
		# for the next iteration
		for i in adj_list[u]:
			if (result[i] != -1):
				available[result[i]] = False
 
	# Print the result
	#for u in range(V):
	#	print("Vertex", u, " --->  Color", result[u])
	#print(result)
	#for v in range(num_of_nodes):
	#	print(f'Color assigned to vertex {v} is {colors[result[v]]}')
	#return len(list(set(list(result.values()))))
	return len(list(set(result)))


def is_bipartite(adj_list, c):
	""" Checks if graph is bipartite by giving it colours"""
	# Colours are just True and False
	colours = dict()

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