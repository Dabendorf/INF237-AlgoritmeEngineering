# https://uib.kattis.com/problems/hoppers

import sys
from typing import Tuple
from collections import defaultdict

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

	components = list()
	while todo:
		res = BFS(todo.pop(), adj_list = adj_list_direct)
		components.append(next(iter(res)))
		for i in res:
			if i in todo:
				todo.remove(i)

	is_bip = is_bipartite(adj_list=adj_list_direct, components=components)
	
	if is_bip:
		print(len(components))
	else:
		print(len(components)-1)

def BFS(s, adj_list):
	output_list = set()
	visited = defaultdict(lambda: False)

	queue = [s]
	visited[s] = True

	while queue:
		s = queue.pop()

		if s != None:
			output_list.add(s)

		for i in adj_list[s]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True

	return output_list

def is_bipartite(adj_list, components):
	colours = dict()

	for c in components:
		queue = [c]
		colours[c] = True
		while queue:
			el = queue.pop()
			for neighbour in adj_list[el]:
				if neighbour in colours:
					if colours[el] == colours[neighbour]:
						return False
				else:
					queue.append(neighbour)
					colours[neighbour] = not colours[el]
	return True


if __name__ == "__main__":
	main()