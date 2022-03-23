# https://uib.kattis.com/problems/mapcolouring

import sys
from collections import defaultdict

if len(sys.argv) > 1:
	debug = print
else:
	debug = lambda *_,**__:None

""" Colour a map. Determine how many colours are needed. If more than 4 are needed, just output "many"

	Solution:
	- There are some initial if conditions to make things easier
	- If there are no edges, only one colour is needed
	- If graph is fully connected, it needs as many colours as nodes
	- I reused my bipartite matching algorithm to check if something is 2-colourable
	- If nothing of these works, it checks if the graph is 3 colourable or 4 colourable
	- If none of these work, it returns "many"
	
	Functionality of the {3,4}-colourable algorithm:
	- The algorithm takes five arguments, which are the adjacency list, the colour list, the number of colours and the number of nodes
	- The fifth one changes in each recursion step, which is the number of the current node going up
	- The base case is that the current node number is bigger than the number of nodes, so every node got colours
	- Otherwise, the algorithm goes through all colours and tries each of them on the node
	- If a neighbour has the same colour, this recursion step gets trashed, if there is an success, the algorithm continues recursively with the next node
	
	"""
def main():
	num_of_testcases = int(sys.stdin.readline())
	# <= 33 testcases
	# <= 16 countries
	# <= 120 borders

	for test_num in range(num_of_testcases):
		debug(f"Test nummer: {test_num}")
		adj_list = defaultdict(lambda: set())
		num_nodes, num_edges = list(map(int, sys.stdin.readline().strip().split(" ")))
		
		for _ in range(num_edges):
			node_a, node_b = list(map(int, sys.stdin.readline().strip().split(" ")))
			
			adj_list[node_a].add(node_b)
			adj_list[node_b].add(node_a)

		# if no edges, one colour is possible
		if num_edges == 0:
			print(1)
		elif num_edges == (num_nodes * (num_nodes-1))/2:
			# if graph is fully connected, it needs num_of_nodes colours
			if num_nodes < 5:
				print(num_nodes)
			else:
				print("many")
		else:
			# check if bipartite
			if is_bipartite(adj_list, 0):
				print(2)
			else:
				debug("1 or 2 colours not possible, check 3 or 4")
				debug(f"Num of nodes: {num_nodes}, num of edges: {num_edges}")
				# check if it works for 3 or 4, if not return many
				found = False
				for num_of_colours in range(3,5):
					colours = [None] * num_nodes
					colours[0] = 1
					if graph_colouring(adj_list, colours, num_of_colours, 1, num_nodes):
						print(num_of_colours)
						found = True
						break
				if not found:
					print("many")

			""" An extracase for planar graphs which for same weird reason doesnt work
			elif num_edges <= 3*num_nodes - 6:
				# graph is planar
				#print("check if 3 or 4 colourable")
				output = greedy_colouring(adj_list, num_nodes)
				if output > 4:
					print(4)
				else:
					print(output)"""

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
	""" Checks if graph is bipartite by giving it colours
		Code reused from my graphs 1 solutions"""
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