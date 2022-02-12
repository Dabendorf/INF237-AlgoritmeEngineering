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
	q = []
	num_of_nodes = len(adj_list.items())
	print("num of nodes: "+str(num_of_nodes))
	
	dist = dict()
	#pre = dict()

	for i in range(num_of_nodes):
		dist[i] = float('inf')

	for i in adj_list[start]:
		q.append((i[1], i[0]))
		#q.put((G[s][i]["weight"],i))


	dist[start] = 0
	#q.put((0, s))
	q.append((0, start))
	heapq.heapify(q)

	visited = []
	print(f"Initial neighbours: {q}")
	while q:
		u = heapq.heappop(q)

		if u[1] not in visited:
			print("========")
			print("Next node: "+str(u[1]))
			for v in adj_list[u[1]]:
			#for v in G.neighbors(u):
				if v[0] not in visited:
					print("Neighbour: "+str(v[0]))
					alt = dist[u[1]] + v[1]
					print(f"alt {alt}")
					#alt = dist[u] + G[u][v]['weight']
					print("Alternative distance: "+str(alt))
					print(v)
					print("Old distance: "+str(dist[v[0]]))
					if alt < dist[v[0]]:
						dist[v[0]] = alt
						#q.put((alt, v))
						print(f"klingeer {v}")
						heapq.heappush(q, (v[1], v[0]))
						#pre[v] = u

			print("Distances: ")
			print(dist)

			visited.append(u[1])

	print("Visited:")
	print(visited)
	print("Distances: ")
	print(dist)

if __name__ == "__main__":
	main()