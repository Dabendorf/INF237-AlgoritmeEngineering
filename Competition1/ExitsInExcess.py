import sys
from collections import defaultdict
import math
import heapq

def main():
	num_of_rooms, num_of_corridors = list(map(int, sys.stdin.readline().strip().split()))

	adj_list = defaultdict(lambda: [])
	room_num = list()
	edge_list = set()
	for i in range(num_of_corridors):
		fra, til = list(map(int, sys.stdin.readline().strip().split()))
		adj_list[fra].append(til)
		edge_list.add((fra, til))
		room_num.append((fra, til))

	print(adj_list)
	print(room_num)
	print(f"Edges: {edge_list}")
	print(f"Edges bfs: {bfs(1, adj_list)}")
	diff = edge_list- bfs(1, adj_list)
	print(diff)

def bfs(s, adj_list):
	""" Its a BFS. The way a BFS always has behaved"""
	output_list = set()
	list_edges = set()
	visited = defaultdict(lambda: False)

	# Queue starts with start node
	queue = [s]
	visited[s] = True

	# While queue, go through them
	while queue:
		s = queue.pop()

		if s != None:
			output_list.add(s)

		# Mark neighbours as visited and add to queue
		for i in adj_list[s]:
			if visited[i] == False:
				queue.append(i)
				list_edges.add((s,i))
				visited[i] = True

	# Returns list of all visited nodes
	return list_edges


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
					for id, scheissverein in enumerate(pq):
						if scheissverein[1] == neighbour:
							to_delete = id
							break
					del pq[to_delete]
					shortest[neighbour] = w

			heapq.heapify(pq)
	
	print(f"{edge_sum}")"""

		

if __name__ == "__main__":
	main()