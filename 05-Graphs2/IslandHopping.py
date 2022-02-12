# https://uib.kattis.com/problems/islandhopping

import sys
from collections import defaultdict
from queue import PriorityQueue
import math

def main():
	num_of_cases = int(sys.stdin.readline())

	for _ in range(num_of_cases):
		num_of_islands = int(sys.stdin.readline())

		endpoints = list()
		adj_list = defaultdict(lambda: [])
		weight_list = dict()

		for idx_a in range(num_of_islands):
			a = [float(i) for i in sys.stdin.readline().strip().split(" ")]

			for idx_b, b in enumerate(endpoints):
				dist = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
				adj_list[idx_a].append(idx_b)
				adj_list[idx_b].append(idx_a)
				weight_list[(idx_a, idx_b)] = dist
				weight_list[(idx_b, idx_a)] = dist

			endpoints.append(a)

		pq = PriorityQueue()
		visited = defaultdict(lambda: False)
		visited[0] = True
		for neighbour in adj_list[0]:
			pq.put((weight_list[0, neighbour], neighbour))

		edge_sum = 0
		while not pq.empty():
			next_smallest_node = pq.get()

			if not visited[next_smallest_node[1]]:
				visited[next_smallest_node[1]] = True
				edge_sum += next_smallest_node[0]
				for neighbour in adj_list[next_smallest_node[1]]:
					if not visited[neighbour]:
						pq.put((weight_list[next_smallest_node[1],neighbour], neighbour))
		
		print(f"{edge_sum}")

		

if __name__ == "__main__":
	main()