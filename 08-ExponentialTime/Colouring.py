# https://open.kattis.com/problems/coloring

import sys
from collections import defaultdict

""" Problem

	Solution:
	- 
	"""
def main():
	num_of_nodes = int(sys.stdin.readline())

	adj_list = defaultdict(lambda: set())
	edges_existing = False
	for idx in range(num_of_nodes):
		neighbours = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		
		for n in neighbours:
			edges_existing = True
			adj_list[idx].add(n)
			adj_list[n].add(idx)

	for key, val in adj_list.items():
		adj_list[key] = list(val)

	# if no edges, one colour is possible
	if not edges_existing:
		print(1)
	else:
		# check if bipartite
		if is_bipartite(adj_list, 0):
			print(2)
		else:
			# check if it works for 3 or 4, if not return many
			found = False
			for num_of_colours in range(3,11):
				colours = [None] * num_of_nodes
				colours[0] = 1
				if graph_colouring(adj_list, colours, num_of_colours, 1, num_of_nodes):
					print(num_of_colours)
					found = True
					break
			if not found:
				print(11)

def graph_colouring(adj_list, colours, num_of_colours, current_node, num_nodes):
	""" This checks if the graph can be coloured with a certain amount of colours
		It is an recursive algorithm, taking 5 parameters

		:param adj_list: The adjacency list of the graph
		:param colours: A list of colours for each country-index
		:param num_of_colours: Number of colours available
		:param current_node: Current node number to look at
		:param num_nodes: number of nodes (countries)

		The adjacency list, the colour list, the number of colours and number of nodes stay the same
		There is one variable changing in each iteration, which is the node, since the algorithm goes through all nodes after each other
		The base case is that the current node number is bigger than the number of nodes, so every node got colours
		Otherwise, the algorithm goes through all colours and tries each of them on the node
		If a neighbour has the same colour, this recursion step gets trashed, if there is an success, the algorithm continues recursively with the next node
	"""
	# Basecase; if node number is bigger than actual number of nodes, return true since algorithm finished
	if current_node >= num_nodes:
		return True

	# Go through all colours available for that node
	for current_colour in range(1, num_of_colours+1):
		valid = True

		# Check if any neighbour has the same colour
		# If so, the colour is not valid
		for neighbour in adj_list[current_node]:
			if current_colour == colours[neighbour]:
				valid = False
		
		# If the colour is valid, colour it with that colour and call recursion
		if valid:
			colours[current_node] = current_colour
			if graph_colouring(adj_list, colours, num_of_colours, current_node+1, num_nodes):
				return True
		colours[current_node] = 0

	# Colouring not possible if the code gets to this point
	return False


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