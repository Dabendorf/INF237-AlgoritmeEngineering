# https://uib.kattis.com/problems/spiderman

import sys
from typing import Tuple
from collections import defaultdict

""" There is a list of numbers which represent movements either up or down.
	Spiderman starts at level 0 and he does the moves in order, always going up or down.
	Find out if its possible to end the workout of movements at zero again, without getting below zero.
	If it is possible, find the order of moves of the solution with lowest maximum height.

	Solution:
	-
	"""
def main():
	num_of_cases = int(sys.stdin.readline())

	for case in range(num_of_cases*2):
		print("==========")
		number_of_moves = int(sys.stdin.readline().strip())
		moves_str = sys.stdin.readline().strip().split(" ")
		moves = [int(i) for i in moves_str]
		sum_moves = sum(moves)
		height = sum_moves//2+1

		dp = [[None for _ in range(number_of_moves+1)] for _ in range(height)]
		
		for h in range(height):
			dp[h][0] = 0

		print(moves)
		start_points = {0}
		for move_ind, move in enumerate(moves):
			for el in start_points:
				new_start_points = set()
				old_val = dp[el][move_ind]
				if el+move < height:
					to_go_to = el+move
					new_val = max(old_val, to_go_to)
					if dp[to_go_to][move_ind+1] == None:
						dp[to_go_to][move_ind+1] = new_val
					else:
						dp[to_go_to][move_ind+1] = min(dp[to_go_to][move_ind+1], new_val)
					new_start_points.add(to_go_to)
				if el-move > -1:
					to_go_to = el-move
					new_val = max(old_val, to_go_to)
					if dp[to_go_to][move_ind+1] == None:
						dp[to_go_to][move_ind+1] = new_val
					else:
						dp[to_go_to][move_ind+1] = min(dp[to_go_to][move_ind+1], new_val)
					new_start_points.add(to_go_to)
			start_points = new_start_points
		
		if dp[0][number_of_moves] == None:
			print("IMPOSSIBLE")
		else:
			#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in dp]))
			curr_height = 0
			overall_str = ""
			for i in range(number_of_moves, 0, -1):
				#print(f"New iteration on move {i}")
				up = curr_height + moves[i-1]
				down = curr_height - moves[i-1]
				#print(f"{i-1} {up}")
				#print(f"{i-1} {down}")

				if up < height and dp[i-1][up] != None:
					if down > -1 and dp[i-1][down] != None:
						# both possible
						#print(f"{i-1} {up}, {i-1} {down}")
						if dp[i-1][up] < dp[i-1][down]:
							overall_str += "U"
							curr_height = up
							#print("move up")
						else:
							overall_str += "D"
							curr_height = down
							#print("move down")
					else:
						# only up possible
						overall_str += "U"
						curr_height = up
						#print("move up")
				else:
					# only down possible
					overall_str += "D"
					curr_height = down
					#print("move down")

			print(overall_str)


if __name__ == "__main__":
	main()