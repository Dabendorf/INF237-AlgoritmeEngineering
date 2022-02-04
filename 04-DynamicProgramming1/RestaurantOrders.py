# https://open.kattis.com/problems/orders

import sys
from collections import defaultdict

def main():
	sys.stdin.readline()
	item_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]
	sys.stdin.readline()
	order_costs = [int(i) for i in sys.stdin.readline().strip().split(" ")]

	max_weight = max(order_costs)
	
	ambiguities, paths, M = knapsack(weight=max_weight, item_costs=item_costs, to_search=order_costs)

	# Output
	for idx, weight in enumerate(order_costs):
		if M[idx] != weight:
			print("Impossible")
		else:
			if weight in ambiguities:
				print("Ambiguous")
			else:
				for x in paths[weight]:
					print(x, end=" ")
				print("")
				#print(" ".join(str(x) for x in paths[weight]))


def knapsack(weight: int, item_costs: list, to_search: list):
	""" Subroutine calculating one knapsack """
	num_of_items = len(item_costs)

	# Initialise memory
	M = [0]*(weight+1)
	M[0] = 0

	paths = defaultdict(lambda: list())
	paths[0] = [[]]

	ambiguities = set()

	# Knapsack algoritm with weight = value (subsetsum?)
	for w in range(weight+1):
		for i in range(num_of_items):
			ic = item_costs[i]
			if ic <= w:
				# Subproblem formula
				pick_item_sum = M[w-ic] + ic
				if M[w] <= pick_item_sum:
					M[w] = pick_item_sum
					if (w-ic) in ambiguities:
						ambiguities.add(w)
						paths[w] = []
					else:
						if len(paths[w-ic]) > 0:
							gedoens = paths[w-ic][0]
							ind = bs(gedoens, 0, len(gedoens)-1, i+1)
							new_el = gedoens[:ind] + [i+1] + gedoens[ind:]

							len_old_list = len(paths[w])
							if new_el not in paths[w]:
								paths[w].append(new_el)
								if len_old_list > 0:
									ambiguities.add(w)
	for k, v in paths.items():
		if len(v)>0:
			paths[k] = v[0]
	
	results = []
	for ind, el in enumerate(to_search):
		results.append(M[el])

	to_search = None
	M = None

	return ambiguities, paths, results

def bs(el_list, l, r, x):
	while l <= r:
		mid = l+(r-l)//2

		if el_list[mid] == x:
			return mid
		elif el_list[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return l # returns position where it would be inserted

if __name__ == "__main__":
	main()