import sys
from typing import Tuple
from collections import defaultdict

def main():
	encrypted = sys.stdin.readline().strip()
	key = sys.stdin.readline().strip()

	azlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	letter_ind = dict()

	for idx, el in enumerate(azlist):
		letter_ind[el] = idx

	print(augustus(encrypted, key, azlist, letter_ind))

def augustus(todecode, key, azlist, letter_ind):
	output_string = ""
	#print(f"Len key: {len(key)}")
	for idx, letter in enumerate(todecode):
		idx_temp = idx%len(key)
		ord_num_of_letter = letter_ind[letter] - letter_ind[key[idx_temp]]

		
		#print(f"idx: {idx} {idx_temp} {key[idx_temp]}")
		#print(f"letter: {letter} {letter_ind[letter]}")

		if ord_num_of_letter % 2 == 0:
			output_letter = caesar(letter, -letter_ind[key[idx_temp]], azlist, letter_ind)
			output_string += output_letter
		else:
			output_letter = caesar(letter, +letter_ind[key[idx_temp]], azlist, letter_ind)
			output_string += output_letter
	return output_string

def caesar(letter, key, azlist, letter_ind):
	return azlist[((letter_ind[letter]+key) % 26)]

if __name__ == "__main__":
	main()