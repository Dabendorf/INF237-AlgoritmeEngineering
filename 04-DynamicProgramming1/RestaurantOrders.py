# https://open.kattis.com/problems/orders

import sys
from typing import Tuple
from collections import defaultdict

def main():
	num_of_items = int(sys.stdin.readline())
	item_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	num_of_orders = int(sys.stdin.readline())
	order_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]

	for i in order_costs:
		print(knapsack(weight=i, item_costs=item_costs))
		

def knapsack(weight: int, item_costs: list):
	""" Subroutine calculating one knapsack """
	num_of_items = len(item_costs)

	# Initialise memory
	M = [0]*(weight+1)
	M[0] = 0

	#print(f"Knapsack with weight {weight}")

	paths = defaultdict(lambda: list())
	paths[0] = [[]]

	# Knapsack algoritm with weight = value (subsetsum?)
	for w in range(weight+1):
		for i in range(num_of_items):
			if item_costs[i] <= w:
				# Subproblem formula
				pick_item_sum = M[w-item_costs[i]] + item_costs[i]
				if M[w] <= pick_item_sum:
					M[w] = pick_item_sum
					for gedoens in paths[w-item_costs[i]]:
						paths[w].append(gedoens + [i+1])

				# M[w] = max(M[w], M[w-item_costs[i]] + item_costs[i])

	# Output
	if M[weight] != weight:
		return "Impossible"
	else:
		a = sorted(paths[w][0])
		amb = False
		for l in range(1, len(paths[w])):
			n = sorted(paths[w][l])
			if a != n:
				amb = True
				break
		
		if amb:
			return "Ambiguous"
		else:
			return " ".join(str(x) for x in a)

if __name__ == "__main__":
	main()