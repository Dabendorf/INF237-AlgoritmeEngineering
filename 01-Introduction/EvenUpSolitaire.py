# https://uib.kattis.com/problems/evenup

import sys
from itertools import groupby

def main():
	debug = True
	_ = sys.stdin.readline()

	for line in sys.stdin:
        # Reads one list of integers per line
		case_str = line.strip().split(" ")
		numbers = [int(i) for i in case_str]

	bool_list = [True if x%2==0 else False for x in numbers]

	count_dups = [(sum(1 for _ in group)%2, m) for m, group in groupby(bool_list)]
	
	if debug:
		print(numbers)
		print(bool_list)
		print(count_dups)

	changed = True
	while changed:
		changed = False
		new_list = list()
		len_list = len(count_dups)
		for idx in range(len_list):
			quantity, el = count_dups[idx]

			if quantity == 0:
				changed=True
			else:
				if idx > 0:
					quantityPre, elPre = count_dups[idx-1]
					if el == elPre:
						if quantityPre == 1 and quantity == 1:
							changed = True
							new_list.pop()
					else:
						new_list.append(count_dups[idx])

				else:
					new_list.append(count_dups[idx])
		count_dups = new_list
		if debug:
			print(count_dups)
	
	if debug:
		print(count_dups)
	output = sum(quantity for quantity, _ in count_dups)
	print(output)


		

if __name__ == "__main__":
	main()