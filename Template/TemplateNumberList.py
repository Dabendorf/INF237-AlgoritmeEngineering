import sys
from typing import Tuple
from collections import defaultdict

def main():
	num_of_cases = sys.stdin.readline()

	for line in sys.stdin:
        # Reads one list of integers per line
		case_str = line.strip().split(" ")
		case = [int(i) for i in case_str]
		

if __name__ == "__main__":
	main()