import sys
import re

def main():
	lines = sys.stdin.readlines()
	
	num_testcases = len(lines)//2

	for i in range(num_testcases):
		pattern = lines[2*i].strip()
		text = lines[2*i+1].strip()
		#print(pattern)
		#print(text)

		occurrences = [str(occurence.span()[0]) for occurence in re.finditer(pattern, text)]
		print(" ".join(occurrences))

def phash(word, A=3, B=97):
	n = len(word)
	return (sum(ord(e) * (A ** (n - i - 1)) for i, e in enumerate(word)) % B)

def rolling_hash(text, k):
	A = 3
	B = 97
	h = [0] * len(text)
	for i in range(len(text) - 5):
		h[i] = window(text, k, i, h[i - 1], A, B)
	return h

def window(text, k, idx, cur_hash, A, B):
	if idx == 0:
		return phash(text[:k], A, B)
	cur_hash -= ord(text[idx - 1]) * (A ** (k - 1))
	cur_hash *= A
	cur_hash += ord(text[idx + k - 1])
	return cur_hash % B
		

if __name__ == "__main__":
	main()