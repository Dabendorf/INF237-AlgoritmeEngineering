# https://uib.kattis.com/problems/mapcolouring

import sys
from collections import defaultdict
from random import shuffle

""" Problem

	Solution:
	- 
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

		#output = greedy_colouring(adj_list, num_nodes)
		#print(output)
		

		if num_edges == 0:
			print(1)
		elif num_edges == (num_nodes * (num_nodes-1))/2:
			if num_nodes < 5:
				print(num_nodes)
			else:
				print("many")
		else:
			if is_bipartite(adj_list, 0):
				print(2)
			else:
				found = False
				for i in range(2,5):
					ignore_set = set()
					for key, val in adj_list.items():
						num_neighbours = len(list(val))
						if num_neighbours == 0:
							ignore_set.add(key)
						if num_neighbours == 1:
							ignore_set.add(key)
							adj_list[list(val)[0]].remove(key)
					if graphColoring(adj_list, i, 0, [0]*num_nodes, num_nodes, ignore_set):
						print(i)
						found = True
						break
				if not found:
					print("many")
				"""output = greedy_colouring(adj_list, num_nodes)
				run_num = 300
				if run_num > 0 and output > 3:
					output = min(greedy_colouring(adj_list, num_nodes), output)
					run_num -= 1
				print(output)"""
				#print("check if 3, 4 or many colourable")

			"""elif num_edges <= 3*num_nodes - 6:
				# graph is planar
				#print("check if 3 or 4 colourable")
				output = greedy_colouring(adj_list, num_nodes)
				if output > 4:
					print(4)
				else:
					print(output)"""
def isSafe(adj_list, color, num_nodes):
	for i in range(num_nodes):
		for j in range(i + 1, num_nodes):
			if j in adj_list[i] and color[j] == color[i]:
				return False
	return True
 
# /* This function solves the m Coloring
# problem using recursion. It returns
# false if the m colours cannot be assigned,
# otherwise, return true and prints
# assignments of colours to all vertices.
# Please note that there may be more than
# one solutions, this function prints one
# of the feasible solutions.*/
def graphColoring(adj_list, m, i, color, num_nodes, ignore_set):
	# if current index reached end
	if i == num_nodes:
 
		# if coloring is safe
		if isSafe(adj_list, color, num_nodes):
			# Print the solution
			#printSolution(color)
			return True
		return False
 
	# Assign each color from 1 to m
	if i in ignore_set:
		color[i] = 0

		# Recur of the rest vertices
		if graphColoring(adj_list, m, i + 1, color, num_nodes, ignore_set):
			return True
		color[i] = 0
		return False
	else:
		for j in range(1, m + 1):
			color[i] = j
	
			# Recur of the rest vertices
			if graphColoring(adj_list, m, i + 1, color, num_nodes, ignore_set):
				return True
			color[i] = 0
		return False

def greedy_colouring(adj_list, num_of_nodes):
	colours = [None] * num_of_nodes
	colours[0] = 0

	node_list = list(range(num_of_nodes))
	shuffle(node_list)
	
	for node_idx, node in enumerate(node_list):
		if node_idx == 0:
			continue
		#print(f"Node: {node}, adj_list: {adj_list[node]}")
		#print(f"|V|: {num_of_nodes}, adj_list={adj_list}")
		colours_used_redundant = [neighbour for neighbour in adj_list[node] if colours[neighbour] is not None]
		colours_used = set(colours_used_redundant)
		#print(f"Colours used for edge neighbours {node}: {colours_used}")

		next_col = 4
		for i in range(0, 3):
			if i not in colours_used:
				next_col = i
				break

		colours[node] = next_col
		if next_col == 4:
			return 5
	
	return len(list(set(colours)))

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