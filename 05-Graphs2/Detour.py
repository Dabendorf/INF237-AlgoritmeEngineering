# https://open.kattis.com/problems/detour

import sys
from typing import Tuple
from collections import defaultdict
import heapq

""" We drive from node 0 to node 1. There are many intersections and for each of them,
	there is an unique shortest path to 1.
	We are not allowed to take any shortest direction at any intersection (node)
	Print a path were this is possible or output impossible if there is no such path

	Solution:
	- Dijkstra to find the shortest edges from each node
	- Then removing those nodes, we run a BFS
	"""
def main():
	n, m = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	#print(n)
	#print(m)

	adj_list = defaultdict(lambda: [])
	for _ in range(m):
		i, j, cost = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		adj_list[i].append((j, cost))
		adj_list[j].append((i, cost))

	#print(f"Adj: {dict(adj_list)}")

	adj_list = dijkstra_remover(adj_list, 1, 0, n)
	#print(dijkstra(adj_list, 0, 1, n))
	print(bfs(0, adj_list, n, 1))

def dijkstra_remover(adj_list, start, end, num_of_cities):
	""" This is an altered dijkstra funksjon which outputs the paths of 
		every shortest way from a node, and a function deleting those edges"""
	visited = [False] * num_of_cities
	dist = [float("inf")] * num_of_cities
	path = [None] * num_of_cities

	q = []

	dist[start] = 0
	heapq.heappush(q, (0, start))

	while q:
		distance_u, u = heapq.heappop(q)
		visited[u] = True
		for v, distance_v in adj_list[u]:
			if not visited[v]:
				new_dist = distance_u + distance_v
				if new_dist < dist[v]:
					dist[v] = new_dist
					path[v] = u
					heapq.heappush(q, (new_dist, v))

	new_adj_list = defaultdict(lambda: [])

	for k, v in adj_list.items():
		for el in v:
			if el[0] != path[k]:
				new_adj_list[k].append(el[0])

	return new_adj_list

def bfs(s, adj_list, num_of_cities, end):
	""" Its a BFS. The way a BFS always has behaved"""

	# Queue starts with start node
	queue = [s]
	visitedFrom = [None] * num_of_cities
	visitedFrom[s] = -1

	# While queue, go through them
	while queue:
		s = queue.pop()

		# Mark neighbours as visited and add to queue
		for i in adj_list[s]:
			if visitedFrom[i] == None:
				queue.append(i)
				visitedFrom[i] = s

	#print(visitedFrom)

	# Return either the path or impossible

	if visitedFrom[1] == None:
		return "impossible"
	else:
		counter_len = 1
		curr = 1
		output_str = "1"

		while curr != 0:
			curr = visitedFrom[curr]
			output_str = str(curr)+" "+output_str
			counter_len += 1
			#print(output_str)
		return str(counter_len)+ " "+output_str

if __name__ == "__main__":
	main()