# https://open.kattis.com/problems/bing

from sys import stdin
from collections import defaultdict

""" There are n words and for every word we want to now of how many words coming before the new word is the prefix of

	Solution:
	- There is a counter dictionary which counts how often a prefix has been seen before
	- For every word, I increase the number of every prefix of this word by 1,
		counting that this prefix has been seen one more time
	- In the end, for every word, one just goes into the dictionary and looks how often it has already seen that prefix
	- That result must be substracted by one since the word itself counted as one already
	"""
def main():
	num_of_words = int(stdin.readline())

	counter = defaultdict(lambda: 0)

	# Go through words
	for i in range(num_of_words):
		new_word = stdin.readline().strip()

		st = ""
		# Go through all letters
		for letter in new_word:
			st += letter
			# Add to counter
			counter[st] += 1

		# Substract 1 from solution since word is substring of itself
		print(counter[new_word]-1)

if __name__ == "__main__":
	main()