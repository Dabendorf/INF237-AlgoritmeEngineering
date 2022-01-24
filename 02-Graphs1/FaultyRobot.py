from random import random
import sys
from typing import Tuple
from collections import defaultdict

from sympy import adjoint

def main():
	num_of_nodes, num_of_edges = sys.stdin.readline().strip().split(" ")

	adj_list_direct = defaultdict(lambda: set())
	forced_moves = dict()

	visited_nodes = defaultdict(lambda: set())

	possible_end_nodes = set()

	node_list = set()
	
	for line in sys.stdin:
        # Reads one list of integers per line
		case_str = line.strip().split(" ")
		case = [int(i) for i in case_str]
		fra, til = case

		if fra > 0:
			adj_list_direct[fra].add(til)
			node_list.add(til)
		else:
			forced_moves[-fra] = til
			node_list.add(til)
	
	next_node_list_wrong = defaultdict(lambda: set())
	next_node_list_correct = defaultdict(lambda: set())
	for node in node_list:
		next_node_list_correct[node] = next_node(node=node, forced_moves=forced_moves, adj_list_direct=adj_list_direct, random_allowed=False)
		next_node_list_wrong[node] = next_node(node=node, forced_moves=forced_moves, adj_list_direct=adj_list_direct, random_allowed=True)

	for node in node_list:
		already_visited = set()
		wrong_trekk_gjort = False
		paths_left = next_node_list_wrong[node]

		#while paths_left:
		#	for n in paths_left:


	print(f"Nodes: {node_list}")
	print(f"Adjacency: {adj_list_direct}")
	print(f"Forced: {forced_moves}")
	print(f"Visited: {visited_nodes}")
	print(f"Possible endnodes: {possible_end_nodes}")
	print(f"Next nodes correct: {next_node_list_correct}")
	print(f"Next codes false: {next_node_list_wrong}")

def next_node(node: int, forced_moves, adj_list_direct, random_allowed = False):
	if random_allowed:
		list_poss_nodes = set()
		if node in forced_moves:
			list_poss_nodes.add(forced_moves[node])
		if node in adj_list_direct:
			for moves in adj_list_direct[node]:
				list_poss_nodes.add(moves)
		return list_poss_nodes
	else:
		if node in forced_moves:
			return {forced_moves[node]}
		else:
			return set()

if __name__ == "__main__":
	main()