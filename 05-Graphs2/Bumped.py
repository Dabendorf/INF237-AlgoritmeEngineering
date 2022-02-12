# https://uib.kattis.com/problems/bumped

import sys
from typing import Tuple
from collections import defaultdict
import heapq

def main():
	n, m, f, s, t = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	print(n)
	print(m)
	print(f)
	print(s)
	print(t)

	adj_list = defaultdict(lambda: [])
	for _ in range(m):
		i, j, cost = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		adj_list[i].append((j, cost))
		adj_list[j].append((i, cost))

	flights = defaultdict(lambda: [])
	for _ in range(f):
		u, v = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		flights[u].append(v)
		flights[v].append(u)

	print(adj_list)
	print(flights)
	print(dijkstra(adj_list, s, t))

def dijkstra(adj_list, start, end):
	# Priority Queue
	q = []
	num_of_nodes = len(adj_list.items())
	
	# Distances
	dist = dict()

	# Initially infinite distances
	for i in range(num_of_nodes):
		dist[i] = float('inf')

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

		if not visited[u[1]]:
			for v in adj_list[u[1]]:
				if not visited[v[0]]:
					# Calculate alternative distance
					alt = dist[u[1]] + v[1]

					# If its smaller than original distance, replace it
					if alt < dist[v[0]]:
						dist[v[0]] = alt
						heapq.heappush(q, (v[1], v[0]))

			visited[u[1]] = True

	print("Visited:")
	print(visited)
	print("Distances: ")
	print(dist)

	return dist[end]

if __name__ == "__main__":
	main()