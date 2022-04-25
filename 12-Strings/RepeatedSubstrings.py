# https://open.kattis.com/problems/repeatedsubstrings

from sys import stdin
from collections import defaultdict

def main():
	word = stdin.readline()
	

def longest_prefix_suffix(pattern):
	n, k = 0, len(pattern)
	lps = [0] * k
	idx = 1

	while idx < k:
		if pattern[idx] == pattern[n]:
			n += 1
			lps[idx] = n
			idx += 1
		else:
			if n != 0:
				n = lps[n - 1]
			else:
				lps[idx] = 0
				idx += 1
	return lps

def kmp(text, pattern, lps):
	n, k = len(text), len(pattern)
	txt_idx, pat_idx = 0, 0

	while txt_idx < n:
		if pattern[pat_idx] == text[txt_idx]:
			txt_idx += 1
			pat_idx += 1
		if pat_idx == k:
			yield txt_idx - k
			pat_idx = lps[pat_idx - 1]
		elif txt_idx < n and pattern[pat_idx] != text[txt_idx]:
			if pat_idx != 0:
				pat_idx = lps[pat_idx - 1]
			else:
				txt_idx += 1

def phash(word, A=3, B=97):
	n = len(word)
	return (sum(ord(e) * (A ** (n - i - 1)) for i, e in enumerate(word)) % B)

def find_all(h, text, word):
	the_hash = phash(word)
	for i, e in enumerate(h):
		if e == the_hash:
			# could be false positive, hence O(k) test:
			if text[i:i + len(word)] == word:
				yield i

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

def trie(words):
	root = {}
	for word in words:
		current = root
		for letter in word:
			current = current.setdefault(letter, {})
		current["*"] = "*"
	return root
		
def find(t, w):
	current = t
	for letter in w:
		if letter not in current:
			return None
		current = current[letter]
	return current

if __name__ == "__main__":
	main()