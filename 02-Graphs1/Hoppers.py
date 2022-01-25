# https://uib.kattis.com/problems/hoppers

import sys
from typing import Tuple
from collections import defaultdict

""" A new virus is spreading only two the neighbours of the neighbours of a infected computer.
	Find out how many connections are missing such that one computer infects all
	
	Solution:
	Find number of connected components via usage of BFS/DFS
	This needs n-1 links between them
	If the graph contains odd-cycle, it possible to spread all of them
	If there is no odd cycle, one more edge needs to be added to obtain that
	Odd cycle detection via bipartite graph detection, looping through the graph given all nodes colours
	
	In the end, return n or n-1 depending on the odd-cycle thing"""
def main():
	N, M = sys.stdin.readline().strip().split(" ")

	adj_list_direct = defaultdict(lambda: set())
	todo = set(range(1, int(N)+1))
	for line in sys.stdin:
		# Reads one list of integers per line
		case_str = line.strip().split(" ")
		case = [int(i) for i in case_str]
		fra, til = case
		adj_list_direct[fra].add(til)
		adj_list_direct[til].add(fra)

	# Counts components
	# Todo are all computers, BFS returns all connected ones and removes todo
	components = list()
	while todo:
		res = bfs(todo.pop(), adj_list = adj_list_direct)
		components.append(next(iter(res)))
		for i in res:
			if i in todo:
				todo.remove(i)

	# Checks if bipartite
	is_bip = is_bipartite(adj_list=adj_list_direct, components=components)
	
	if is_bip:
		print(len(components))
	else:
		print(len(components)-1)

def bfs(s, adj_list):
	""" Its a BFS. The way a BFS always has behaved"""
	output_list = set()
	visited = defaultdict(lambda: False)

	# Queue starts with start node
	queue = [s]
	visited[s] = True

	# While queue, go through them
	while queue:
		s = queue.pop()

		if s != None:
			output_list.add(s)

		# Mark neighbours as visited and add to queue
		for i in adj_list[s]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True

	# Returns list of all visited nodes
	return output_list

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