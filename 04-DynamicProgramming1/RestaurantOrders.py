# https://open.kattis.com/problems/orders

import sys
from typing import Tuple
from collections import defaultdict

def main():
	num_of_items = int(sys.stdin.readline())
	item_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	num_of_orders = int(sys.stdin.readline())
	order_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	
	print(num_of_items)
	print(item_costs)
	print(num_of_orders)
	print(order_costs)

	for i in order_costs:
		print(knapsack(weight=i, item_costs=item_costs))


def knapsack(weight: int, item_costs: list):
	""" Subroutine calculating one knapsack """
	num_of_items = len(item_costs)

	# Initialise memory
	M = [0]*(weight+1)
	M[0] = 0

	print(f"Knapsack with weight {weight}")
	#paths = defaultdict(lambda: list())
	ingoing_path = defaultdict(lambda: [])
	# Knapsack algoritm with weight = value (subsetsum?)
	for w in range(weight+1):
		for i in range(num_of_items):
			if item_costs[i] <= w:
				# Subproblem formula
				pick_item_sum = M[w-item_costs[i]] + item_costs[i]
				if M[w] <= pick_item_sum:
					M[w] = pick_item_sum
					old_path = ingoing_path[w]
					new_path = ingoing_path[w-item_costs[i]] + [item_costs[i]]
					new_path = sorted(new_path)

					print(old_path)
					print(new_path)

					if len(old_path) > 0:
						if old_path != new_path:
							print(f"{w} KLINGER KLINGER KLINGER")
					ingoing_path[w] = new_path

					#paths[w].append(w-item_costs[i])

				# M[w] = max(M[w], M[w-item_costs[i]] + item_costs[i])

	# Output
	"""for k, v in paths.items():
		print(f"{k} {v}")"""
	
	#print(bfs(weight, paths))
	if M[weight] != weight:
		return "Impossible"
	else:
		return M
	
"""def bfs(s, adj_list):
	output_list = set()
	visitedFrom = defaultdict(lambda: set())
	visitedFromOmv = defaultdict(lambda: set())

	# Queue starts with start node
	queue = [s]
	#visited[s] = True

	# While queue, go through them
	while queue:
		s = queue.pop()

		if s != None:
			output_list.add(s)

		# Mark neighbours as visited and add to queue
		for i in adj_list[s]:
			if s not in visitedFrom[i]:
			#if visited[i] == False:
				queue.append(i)
				visitedFrom[i].add(s)
				visitedFromOmv[s].add(i)
				#visited[i] = True

	# Returns list of all visited nodes
	print(visitedFrom)
	print(visitedFromOmv)
	return output_list"""

if __name__ == "__main__":
	main()