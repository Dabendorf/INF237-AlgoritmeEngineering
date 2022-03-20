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
			elif num_edges <= 3*num_nodes - 6:
				print("dadasdasda")
				# graph is planar
				#print("check if 3 or 4 colourable")
				output = greedy_colouring(adj_list, num_nodes)
				if output > 4:
					print(4)
				else:
					print(output)
			else:
				output = greedy_colouring(adj_list, num_nodes)
				run_num = 30
				if run_num > 0 and output > 3:
					output = min(greedy_colouring(adj_list, num_nodes), output)
					print("Kldasda")
					exit(0)
					run_num -= 1
				print(output)
				#print("check if 3, 4 or many colourable")

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
		colours_used_redundant = [neighbour for neighbour in adj_list[node_idx] if colours[neighbour] is not None]
		colours_used = set(colours_used_redundant)
		#print(f"Colours used for edge neighbours {node}: {colours_used}")

		next_col = 4
		for i in range(0, 3):
			if i not in colours_used:
				next_col = i
				break

		colours[node_idx] = next_col
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