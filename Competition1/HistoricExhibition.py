from struct import pack_into
import sys
from typing import Tuple
from collections import defaultdict

def main():
	num_pedestals, num_vases = list(map(int, sys.stdin.readline().strip().split()))

	ped_diam = list()
	adj_list = defaultdict(lambda: set())
	for i in range(num_pedestals):
		a, b = list(map(int, sys.stdin.readline().strip().split()))
		ped_diam.append((a, b))
	vases_diam = list(map(int, sys.stdin.readline().strip().split()))

	print(ped_diam)
	print(vases_diam)

	for idx_v, v in enumerate(vases_diam):
		for idx_p, p in enumerate(ped_diam):
			if v == p[0] or v == p[1]:
				adj_list["v"+str(idx_v+1)].add("p"+str(idx_p+1))
				adj_list["p"+str(idx_p+1)].add("v"+str(idx_v+1))
				#print(f"{idx_v} {idx_p}, {v} {p}")
	
	print(adj_list)

if __name__ == "__main__":
	main()