# https://uib.kattis.com/problems/bumped

import sys
from typing import Tuple
from collections import defaultdict
import heapq

""" There is a road network with costs (directed graphs) and a start and an end point
	Moreover, there is a list of cities connected by a flight and one can use one of these flights
	for free instead of using the rights. Calculate the minimum distance between start and end

	Solution:
	- This is a classic problem for the Dijkstra algorithm
	- However, it must be altered to use the information about one free flight
	"""
def main():
	n, m, f, s, t = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	"""print(n)
	print(m)
	print(f)
	print(s)
	print(t)"""

	adj_list = defaultdict(lambda: [])
	for _ in range(m):
		i, j, cost = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		adj_list[i].append((j, cost))
		adj_list[j].append((i, cost))

	#flights = defaultdict(lambda: [])
	for _ in range(f):
		u, v = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		adj_list[u].append((-v, 0))
		#flights[u].append(v)
		#flights[v].append(u)

	#print(f"Adj: {dict(adj_list)}")
	#print(flights)
	print(dijkstra(adj_list, s, t))

def dijkstra(adj_list, start, end):
	# Priority Queue
	q = []
	num_of_nodes = len(adj_list.items())
	
	# Distances
	dist = [float("inf")] * num_of_nodes
	# Distances with flights
	dist_fl = [float("inf")] * num_of_nodes

	# Initially infinite distances
	"""for i in range(num_of_nodes):
		dist[i] = float('inf')
	for i in range(num_of_nodes):
		dist_fl[i] = float('inf')"""

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
		#print(q)
		u = heapq.heappop(q)
		visited[u[1]] = True
		for v in adj_list[u[1]]:
			#print(f"{u[1]} to {v[0]}")
			if not visited[abs(v[0])]:
				if v[0] < 0:
					is_flight = True
					#v[0] *= -1
					node_num = -v[0]
					node_dist = v[1]
				else:
					is_flight = False
					node_num = v[0]
					node_dist = v[1]
				
				# There was a flight to the original place
				if dist_fl[u[1]] < float("inf"):
					if not is_flight:
						alt = dist_fl[u[1]] + node_dist
						if alt < dist_fl[node_num]:
							dist_fl[node_num] = alt
							heapq.heappush(q, (alt, node_num))

				else:
					# Calculate alternative distance
					alt = dist[u[1]] + node_dist

					# If its smaller than original distance, replace it
					if is_flight:
						# If its a flight
						if alt < dist_fl[node_num]:
							dist_fl[node_num] = alt
							heapq.heappush(q, (alt, node_num))
					else:
						# If not a flight
						if alt < dist[node_num]:
							dist[node_num] = alt
							heapq.heappush(q, (alt, node_num))


	"""print("Visited:")
	print(visited)
	print("Distances: ")
	print(dist)
	print("Flight distances:")
	print(dist_fl)"""

	return min(dist[end], dist_fl[end])

if __name__ == "__main__":
	main()