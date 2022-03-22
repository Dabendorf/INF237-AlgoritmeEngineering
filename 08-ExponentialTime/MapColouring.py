# https://uib.kattis.com/problems/mapcolouring

import sys
from collections import defaultdict

""" Colour a map. Determine how many colours are needed. If more than 4 are needed, just output "many"

	Solution:
	- There are some initial if conditions to make things easier
	- If there are no edges, only one colour is needed
	- If graph is fully connected, it needs as many colours as nodes
	- I reused my bipartite matching algorithm to check if something is 2-colourable
	- If nothing of these works, it checks if the graph is 3 colourable or 4 colourable
	- If none of these work, it returns "many"
	- Functionality of the {3,4}-colourable algorithm
	"""
def main():
	num_of_testcases = int(sys.stdin.readline())
	# <= 33 testcases
	# <= 16 countries
	# <= 120 borders

	for _ in range(num_of_testcases):
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
				# check if it works for 3 or 4, if not return many
				found = False
				for i in range(3,5):
					colours = [None] * num_nodes
					colours[0] = 1
					if graph_colouring(adj_list, colours, i, 1, num_nodes):
						print(i)
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

def graph_colouring(adj_list, colours, n, v, num_nodes):
	""" This checks if the graph can be coloured with a certain amount of colours
		It is an recursive algorithm, taking 5 parameters
		:param adj_list: The adjacency list of the graph
		:param colours: A list of colours for each country-index
		:param n:
		:param v:
		:param num_nodes: number of nodes (countries)
	
	"""
	# Basecase
	if v >= num_nodes:
		return True

	for i in range(1, n+1):
		valid = True

		for j in range(num_nodes):
			if j in adj_list[v] and i == colours[j]:
				valid = False
		
		if valid:
			colours[v] = i
			if graph_colouring(adj_list, colours, n, v+1, num_nodes):
				return True
		colours[v] = 0

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