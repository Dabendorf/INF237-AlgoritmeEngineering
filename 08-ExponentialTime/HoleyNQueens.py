import sys
from typing import Tuple
from collections import defaultdict
from itertools import permutations

def main():
	board_size, num_of_holes = list(map(int, sys.stdin.readline().strip().split(" ")))

	global holes
	holes = set()
	for i in range(num_of_holes):
		# Reads one list of integers per line
		
		hole = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		holes.add((hole[0], hole[1]))
	
	#print(holes)

	l = list(range(board_size))
	perms = permutations(l)
	num_comb = 0

	global table
	table = [[0]*board_size for _ in range(board_size)]

	for perm in perms:
		if put_queen(perm[0], 0) == True:
			if put_queen(perm[1], 1) == True:
				if put_queen(perm[2], 2) == True:
					if put_queen(perm[3], 3) == True:
						if put_queen(perm[4], 4) == True:
							if put_queen(perm[5], 5) == True:
								if put_queen(perm[6], 6) == True:
									if put_queen(perm[7], 7) == True:
										#print_table()
										num_comb += 1
										#print(f"solution{num_comb}")
										#print(" ")
		table = [[0] * board_size for _ in range(board_size)]
	print(num_comb)

def put_queen(x,y):
	global table
	global holes
	if table[y][x] == 0 and (y,x) not in holes:
		for m in range(8):
			table[y][m] = 1
			table[m][x] = 1
			table[y][x] = 2
			if y+m <= 7 and x+m <= 7:
				table[y+m][x+m] = 1
			if y-m >= 0 and x+m <= 7:
				table[y-m][x+m] = 1
			if y+m <= 7 and x-m >= 0:
				table[y+m][x-m] = 1
			if y-m >= 0 and x-m >= 0:
				table[y-m][x-m] = 1
		return True
	else:
		return False
		

if __name__ == "__main__":
	main()