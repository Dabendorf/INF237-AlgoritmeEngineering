import sys
from typing import Tuple
from collections import defaultdict

def main():
	N, M = sys.stdin.readline().strip().split(" ")

	adj_list_direct = defaultdict(lambda: set())
	for line in sys.stdin:
        # Reads one list of integers per line
		case_str = line.strip().split(" ")
		case = [int(i) for i in case_str]
		fra, til = case
		adj_list_direct[fra].add(til)
		adj_list_direct[til].add(fra)
	
	adj_list_level2 = defaultdict(lambda: set())
	for key, value in adj_list_direct.items():
		for node in value:
			adj_list_level2[key].update(adj_list_direct[node])

	#print(adj_list_direct)
	#print(adj_list_level2)

	overall_sets = set()

	for key, value in adj_list_level2.items():
		overall_sets.add(frozenset(value))

	print(overall_sets)
	print(len(overall_sets)-1)

if __name__ == "__main__":
	main()