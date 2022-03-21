import sys
from collections import defaultdict

if len(sys.argv) > 1:
	debug = print
else:
	debug = lambda *_,**__:None

def main():
	height, width = map(int, sys.stdin.readline().strip().split(" "))

	grid = []
	for _ in range(height):
        # Reads one list of integers per line
		#case_str = sys.stdin.readline().strip().split("")
		case_str = list(sys.stdin.readline().strip())
		print(case_str)
		#case = [int(i) for i in case_str]
		grid.append(case_str)

	print(grid)
	
		

if __name__ == "__main__":
	main()