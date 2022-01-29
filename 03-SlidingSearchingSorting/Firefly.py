# https://open.kattis.com/problems/firefly

import sys
from typing import Tuple
from collections import defaultdict

""" There is cave with alternating stalagtites and stalagmites all having a length
	There is a firefly flying horizontally at a chosen level, destroying all obsticles

	Find out what is the minimum number of obsticles to destroy and 
	how many of these levels with that number exist

	Solution:
	- Initialise two lists upper and lower (stalagtites and stalagmites) counting their length appearences
	- Now add them together backwards ([i-1] += [i]) to make a cumulative list
	- Reverse one of the lists and add them together
	- Find the minimum value and how often it appears
	"""
def main():
	N, H = [int(i) for i in sys.stdin.readline().strip().split(" ")]

	height_list_lower = H*[0]
	height_list_upper = H*[0]
	
	for i in range(int(N/2)):
		height_list_lower[int(sys.stdin.readline().strip())-1] += 1
		height_list_upper[int(sys.stdin.readline().strip())-1] += 1

	for i in range(H-1, 0, -1):
		height_list_lower[i-1] += height_list_lower[i]
		height_list_upper[i-1] += height_list_upper[i]

	height_list_upper = height_list_upper[::-1]

	overall_heights = [l+u for l, u in zip(height_list_lower, height_list_upper)]

	m = min(overall_heights)
	counter = overall_heights.count(m)
	print(f"{m} {counter}")
		

if __name__ == "__main__":
	main()