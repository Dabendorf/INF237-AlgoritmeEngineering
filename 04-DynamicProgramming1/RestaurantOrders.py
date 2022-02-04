# https://open.kattis.com/problems/orders

import sys
from typing import Tuple
from collections import defaultdict

def main():
	num_of_items = int(sys.stdin.readline())
	item_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	num_of_orders = int(sys.stdin.readline())
	order_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]

	max_weight = max(order_costs)
	
	ambiguities, paths, M = knapsack(weight=max_weight, item_costs=item_costs)
	#print(ambiguities)

	# Output
	for weight in order_costs:
		if M[weight] != weight:
			print("Impossible")
		else:
			if weight in ambiguities:
				print("Ambiguous")
			else:
				print(" ".join(str(x) for x in paths[weight][0]))


def knapsack(weight: int, item_costs: list):
	""" Subroutine calculating one knapsack """
	num_of_items = len(item_costs)

	# Initialise memory
	M = [0]*(weight+1)
	M[0] = 0

	paths = defaultdict(lambda: list())
	paths[0] = [[]]

	ambiguities = []

	# Knapsack algoritm with weight = value (subsetsum?)
	for w in range(weight+1):
		for i in range(num_of_items):
			if item_costs[i] <= w:
				# Subproblem formula
				pick_item_sum = M[w-item_costs[i]] + item_costs[i]
				if M[w] <= pick_item_sum:
					M[w] = pick_item_sum
					if (w-item_costs[i]) in ambiguities:
						ambiguities.append(w)
					else:
						for gedoens in paths[w-item_costs[i]]:
							ind = bs(gedoens, 0, len(gedoens)-1, i+1)
							new_el = gedoens[:ind] + [i+1] + gedoens[ind:]

							len_old_list = len(paths[w])
							if new_el not in paths[w]:
								paths[w].append(new_el)
								if len_old_list > 0:
									ambiguities.append(w)

	return ambiguities, paths, M

def bs(el_list, l, h, x):
	if h >= l:
		m = (h+l)//2
 		
		if el_list[m] == x:
			return m
		elif el_list[m] > x:
			return bs(el_list, l, m - 1, x)
		else:
			return bs(el_list, m + 1, h, x)
 
	else:
		return l

if __name__ == "__main__":
	main()