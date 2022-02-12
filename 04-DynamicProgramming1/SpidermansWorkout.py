# https://uib.kattis.com/problems/spiderman

import sys

""" There is a list of numbers which represent movements either up or down.
	Spiderman starts at level 0 and he does the moves in order, always going up or down.
	Find out if its possible to end the workout of movements at zero again, without getting below zero.
	If it is possible, find the order of moves of the solution with lowest maximum height.

	Solution:
	- For every testcase there is a dynamic programming table of size (number_of_moves) x (max_possible_height)
	- The first column is zero and it loops through every move (column), creating new entries for every possible new height
	- The stored value is the maximum observed height on that path
	- When two paths merge into one node, we take the lowest maximum
	- The solution is impossible if it did not arrive back at zero height
	- If it is possible, loop backwards through the table, always taking the lowest maximum
	and appending "U" or "D" to the final string depending on the direction chosen
	"""
def main():
	num_of_cases = int(sys.stdin.readline())

	for case in range(num_of_cases):
		try:
			number_of_moves = int(sys.stdin.readline().strip())
			moves_str = sys.stdin.readline().strip().split(" ")
			if number_of_moves > 0:
				moves = [int(i) for i in moves_str]
				sum_moves = sum(moves)
				height = sum_moves//2+1

				dp = [[None for _ in range(number_of_moves+1)] for _ in range(height)]
				
				for h in range(height):
					dp[h][0] = 0

				start_points = {0}
				for move_ind, move in enumerate(moves):
					new_start_points = set()
					for el in start_points:
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
						up = curr_height + moves[i-1]
						down = curr_height - moves[i-1]

						if up < height:
							if dp[up][i-1] != None:
								if down > -1:
									if dp[down][i-1] != None:
										# both possible
										if dp[up][i-1] < dp[down][i-1]:
											overall_str += "D"
											curr_height = up
										else:
											overall_str += "U"
											curr_height = down
									else:
										# only up possible
										overall_str += "D"
										curr_height = up
								else:
									# only up possible
									overall_str += "D"
									curr_height = up
							else:
								# only down possible
								overall_str += "U"
								curr_height = down

						else:
							# only down possible
							overall_str += "U"
							curr_height = down

					print(overall_str[::-1])
		except ValueError:
			exit(0)


if __name__ == "__main__":
	main()