# https://open.kattis.com/problems/detour

import sys
from typing import Tuple
from collections import defaultdict
import heapq

""" Problem description

	Solution:
	- 
	"""
def main():
	n, m = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	print(n)
	print(m)

	adj_list = defaultdict(lambda: [])
	for _ in range(m):
		i, j, cost = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		adj_list[i].append((j, cost))
		adj_list[j].append((i, cost))

	print(f"Adj: {dict(adj_list)}")

	print(dijkstra(adj_list, 0, 1, n))

def dijkstra(adj_list, start, end, num_of_cities):
	# Priority Queue
	q = []
	num_of_nodes = num_of_cities
	
	# Distances
	dist = [float("inf")] * num_of_nodes
	pre = [None] * num_of_nodes

	# Fill priority queue
	for i in adj_list[start]:
		q.append((i[1], i[0]))

	dist[start] = 0
	q.append((0, start))
	heapq.heapify(q)

	# Already visited nodes
	visited = [False] * num_of_nodes

	# While priority queue nodes
	while q:
		u = heapq.heappop(q)
		visited[u[1]] = True
		
		for v in adj_list[u[1]]:
			if not visited[v[0]]:
				# Calculate alternative distance
				alt = dist[u[1]] + v[1]

				# If its smaller than original distance, replace it
				if alt < dist[v[0]]:
					dist[v[0]] = alt
					pre[v[0]] = u[1]
					heapq.heappush(q, (v[1], v[0]))


	print("Visited:")
	print(visited)
	print("Distances: ")
	print(dist)
	print("Pre")
	print(pre)

	return dist[end]

if __name__ == "__main__":
	main()