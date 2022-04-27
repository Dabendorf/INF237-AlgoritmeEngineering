# https://open.kattis.com/problems/clockpictures

from sys import stdin

def main():
	num_handles = int(stdin.readline())

	handles1 = sorted([int(i) for i in stdin.readline().strip().split(" ")])
	handles2 = sorted([int(i) for i in stdin.readline().strip().split(" ")])

	handles1 = handles1 + handles1

	# Calculate distance of handles between each other
	dist1 = [str((handles1[i+1]-handles1[i])%360000) for i in range(len(handles1)-1)]
	dist2 = [str((handles2[i+1]-handles2[i])%360000) for i in range(len(handles2)-1)]

	dist_str1 = "$".join(dist1)
	dist_str2 = "$".join(dist2)

	lps2 = longest_prefix_suffix(dist_str2)
	print(kmp(dist_str1, dist_str2, lps2))
	

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
			#yield txt_idx - k
			return "possible"
			pat_idx = lps[pat_idx - 1]
		elif txt_idx < n and pattern[pat_idx] != text[txt_idx]:
			if pat_idx != 0:
				pat_idx = lps[pat_idx - 1]
			else:
				txt_idx += 1
	return "impossible"

if __name__ == "__main__":
	main()