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
		weight_list = dict()

		for idx_a in range(num_of_islands):
			a = [float(i) for i in sys.stdin.readline().strip().split(" ")]

			for idx_b, b in enumerate(endpoints):
				dist = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
				weight_list[(idx_a, idx_b)] = dist
				weight_list[(idx_b, idx_a)] = dist

			endpoints.append(a)

		pq = []
		visited = [False] * num_of_islands
		visited[0] = True
		not_visited_set = set()
		for neighbour in range(1, num_of_islands):
			pq.append((weight_list[0, neighbour], neighbour))
			not_visited_set.add(neighbour)
		heapq.heapify(pq)

		edge_sum = 0
		while pq:
			next_smallest_node = heapq.heappop(pq)
			d = next_smallest_node[0]
			node = next_smallest_node[1]

			if not visited[node]:
				visited[node] = True
				not_visited_set.remove(node)
				edge_sum += d

				for neighbour in not_visited_set:
					pq.append((weight_list[node,neighbour], neighbour))
					#heapq.heappush(pq, (weight_list[node,neighbour], neighbour))
				heapq.heapify(pq)
		
		print(f"{edge_sum}")

		

if __name__ == "__main__":
	main()