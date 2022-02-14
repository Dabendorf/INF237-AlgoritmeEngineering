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

	new_adj_list = defaultdict(lambda: [])

	for k, v in adj_list.items():
		for el in v:
			#print(k, el)
			if el[0] != pre[k]:
				new_adj_list[k].append(el[0])
				#print(el)

	#print(new_adj_list)
	return new_adj_list

def bfs(s, adj_list, num_of_cities, end):
	""" Its a BFS. The way a BFS always has behaved"""
	output_list = set()
	visited = [False] * num_of_cities

	# Queue starts with start node
	queue = [s]
	visited[s] = True
	visitedFrom = [None] * num_of_cities

	# While queue, go through them
	while queue:
		s = queue.pop()

		if s != None:
			output_list.add(s)

		# Mark neighbours as visited and add to queue
		for i in adj_list[s]:
			if visited[i] == False:
				queue.append(i)
				visitedFrom[i] = s
				visited[i] = True

	# Return either the path or impossible

	if not visited[1]:
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