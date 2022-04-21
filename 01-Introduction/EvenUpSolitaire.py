# https://uib.kattis.com/problems/evenup

import sys
from itertools import groupby

def main():
	_ = sys.stdin.readline()

	for line in sys.stdin:
		# Reads one list of integers per line
		case_str = line.strip().split(" ")
		numbers = [int(i) for i in case_str]

	bool_list = [2 if x%2==0 else 1 for x in numbers]

	count_dups = [(0, m) if (sum(1 for _ in group))%2==0 else (1,m) for m, group in groupby(bool_list)]
	count_dups = [parity for count, parity in count_dups if count > 0]

	changed = True

	while changed:
		old_len = len(count_dups)
		count_dups = [(0, m) if (sum(1 for _ in group))%2==0 else (1,m) for m, group in groupby(count_dups)]
		count_dups = [parity for count, parity in count_dups if count > 0]

		if old_len == len(count_dups):
			changed = False

	print(len(count_dups))

if __name__ == "__main__":
	main()