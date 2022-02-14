# https://uib.kattis.com/problems/islandhopping

import sys
from collections import defaultdict
import math
import heapq

""" There are n islands existing on a map and each of them has a coordinate (x,y) where one can start to build a bridge.
	All islands should become connected and one needs to search the overall minimum length of all bridges to build.

	Solution:
	- This is a minimum spannung tree problem
	- First we calculate all distances of all pairs
		and then use the algorithm of Prim to get the sum of bridge lengths
	"""
def main():
	num_of_cases = int(sys.stdin.readline())

	for _ in range(num_of_cases):
		num_of_islands = int(sys.stdin.readline())

		endpoints = list()
		#weight_list = [[None]*num_of_islands for _ in range(num_of_islands)] 
		edges = list()
		comp = list()
		rank = list()

		for idx_a in range(num_of_islands):
			a = [float(i) for i in sys.stdin.readline().strip().split(" ")]

			comp.append(idx_a)
			rank.append(0)
			for idx_b, b in enumerate(endpoints):
				dist = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
				edges.append((dist, idx_a, idx_b))
				#weight_list[idx_a][idx_b] = dist
				#weight_list[idx_b][idx_a] = dist

			endpoints.append(a)

		sum = 0
		edges = sorted(edges)
		for (dist, u, v) in edges:
			if find(u, comp) != find(v, comp):
				sum += dist
				union(u, v, rank, comp)

		print(sum)
		"""pq = []
		visited = [False] * num_of_islands
		visited[0] = True
		not_visited_set = set()
		shortest = [float("inf")] * num_of_islands
		
		for neighbour in range(1, num_of_islands):
			w = weight_list[0][neighbour]
			pq.append((w, neighbour))
			shortest[neighbour] = w
			not_visited_set.add(neighbour)
		heapq.heapify(pq)

		edge_sum = 0
		while pq:
			#print(str(pq)+"\n\n")
			next_smallest_node = heapq.heappop(pq)
			d = next_smallest_node[0]
			node = next_smallest_node[1]

			if not visited[node]:
				visited[node] = True
				not_visited_set.remove(node)
				edge_sum += d

				for neighbour in not_visited_set:
					w = weight_list[node][neighbour]
					if shortest[neighbour] > w:
						pq.append((w, neighbour))
						shortest[neighbour] = w
				heapq.heapify(pq)
		
		print(f"{edge_sum}")"""

def find(u, comp):
	if comp[u] == u:
		return u
	else:
		parent = find(comp[u], comp)
		comp[u] = parent
		return parent

def union(u, v, rank, comp):
	r1 = find(u, comp)
	r2 = find(v, comp)
	if rank[r1] < rank[r2]:
		comp[r1] = r2
	elif rank[r2] < rank[r1]:
		comp[r2] = r1
	else:
		comp[r1] = r2
		rank[r2] += 1		

if __name__ == "__main__":
	main()