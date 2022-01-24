# https://uib.kattis.com/problems/onewayroads

import sys
from typing import Tuple
from collections import defaultdict

def main():
	num_of_cities, num_of_roads = sys.stdin.readline().strip().split(" ")

	directions_dict = defaultdict(lambda: list())
	for line in sys.stdin:
        # Reads one list of integers per line
		case_str = line.strip().split(" ")
		case = [int(i) for i in case_str]
		fra, til = case
		directions_dict[fra].append(til)
		directions_dict[til].append(fra)
	
	if num_of_cities > num_of_roads:
		print("NO")
		exit(0)

	for key, value in directions_dict.items():
		if len(value) < 2:
			print("NO")
			exit(0)
	
	print("Possibly")

if __name__ == "__main__":
	main()