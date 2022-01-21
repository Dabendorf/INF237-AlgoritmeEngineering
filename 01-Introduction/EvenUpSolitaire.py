# https://uib.kattis.com/problems/evenup

import sys
from typing import Counter, Tuple
from collections import defaultdict

def main():
	num_of_cases = sys.stdin.readline()

	for line in sys.stdin:
        # Reads one list of integers per line
		case_str = line.strip().split(" ")
		numbers = [int(i) for i in case_str]

	bool_list = [True if x%2==0 else False for x in numbers]
	#print(bool_list)

	swapped = True
	siz = len(bool_list)
	while swapped:
		swapped = False
		new_list = list()
		for i in range(siz-1):
			if bool_list[i]!=bool_list[i+1]:
				new_list.append(bool_list[i])
				if i == siz-2:
					new_list.append(bool_list[i+1])
		bool_list = new_list
		new_size = len(bool_list)
		if new_size < siz:
			siz = new_size
			swapped = True
		#print(bool_list)
	#print(bool_list)
	print(len(bool_list))
	
	"""curr_num = numbers.pop()
	counter = 0
	while numbers:
		print(numbers)
		next_num = numbers.pop()
		if (curr_num+next_num) % 2 == 0:
			curr_num = numbers.pop()
		else:
			counter += 1
			curr_num = next_num

	print(counter+1)"""

	"""counter = 0
	i = 0
	while i <= len(numbers)-2:
		#print(i)
		if (numbers[i]+numbers[i+1]) % 2 == 0:
			counter += 2
			#print(i)
			i += 2
		else:
			i += 1
	print(len(numbers)-counter)"""



	"""numbers_new = list()
	removed = True

	while removed:
		removed=False
		numbers_new = list()
		for i in range(len(numbers)-1):
			if (numbers[i]+numbers[i+1]) % 2 == 0:
				removed= True
				i += 1
			else:
				numbers_new.append(numbers[i])
				if i==len(numbers)-2:
					numbers_new.append(numbers[i+1])
		numbers = numbers_new
		#print(numbers)

	print(len(numbers))"""
	
	"""bool_list = [True if x%2==0 else False for x in numbers]
	#print(bool_list)

	from itertools import groupby
	# Source for this codeline: https://stackoverflow.com/questions/39340345/how-to-count-consecutive-duplicates-in-a-python-list
	# it counts how many values following after each other are contained in a list
	count_list =  [sum(1 for _ in group) for _, group in groupby(bool_list)]
	
	result = 0
	for i in count_list:
		if i%2 != 0:
			result += 1

	print(result)"""


	"""curr_val = bool_list[0]
	counter = 0
	for val in range(1, len(bool_list)):
		if curr_val == bool_list[val]:
			counter += 1
		else:
			curr_val = bool_list[val]
			count_list.append(counter)
			counter = 1
		
	print(count_list)

	result = 0
	for i in count_list:
		if i%2 != 0:
			result += 1

	print(result)"""

	"""removed = True
	wrong_until = 0
	while removed:
		removed = False
		for i in range(wrong_until, len(numbers)-1):
			if (numbers[i]+numbers[i+1]) % 2 == 0:
				index = i
				removed = True
				break
			else:
				wrong_until = i+1
				#print(f"wrong until {wrong_until}")
		
		if removed:
			numbers.pop(index)
			numbers.pop(index)
		#print(numbers)

	print(len(numbers))"""

	"""counter = 0
	for i in range(len(numbers)-1):
			if (numbers[i]+numbers[i+1]) % 2 != 0:
				counter += 1

	if counter == 9:
		counter = 10
	print(counter)"""
		

if __name__ == "__main__":
	main()