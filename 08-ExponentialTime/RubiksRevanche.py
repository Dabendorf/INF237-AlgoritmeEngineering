import sys
from collections import defaultdict

if len(sys.argv) > 1:
	debug = print
else:
	debug = lambda *_,**__:None

def main():
	orig_positions = list()
	letter_to_num = {"R":0, "G":1, "B":2, "Y":3}

	for i in range(4):
		line = [letter_to_num[i] for i in list(sys.stdin.readline().strip())]
		orig_positions.extend(line)

	orig_positions = list(range(16))
	debug(orig_positions)
	for i in neighbours(orig_positions):
		print(i)

def swap_positions(pos_old, a, b, c, d, left):
	pos = pos_old.copy()

	if left:
		swap = pos[a]
		pos[a] = pos[b]
		pos[b] = pos[c]
		pos[c] = pos[d]
		pos[d] = swap
	else:
		swap = pos[d]
		pos[d] = pos[c]
		pos[c] = pos[b]
		pos[b] = pos[a]
		pos[a] = swap
	return pos

def neighbours(orig_positions):
	pos = orig_positions.copy()
	yield swap_positions(pos, 0,1,2,3, False)
	yield swap_positions(pos, 4,5,6,7, False)
	yield swap_positions(pos, 8,9,10,11, False)
	yield swap_positions(pos, 12,13,14,15, False)
	yield swap_positions(pos, 0,1,2,3, True)
	yield swap_positions(pos, 4,5,6,7, True)
	yield swap_positions(pos, 8,9,10,11, True)
	yield swap_positions(pos, 12,13,14,15, True)
	yield swap_positions(pos, 0,4,8,12, False)
	yield swap_positions(pos, 1,5,9,13, False)
	yield swap_positions(pos, 2,6,10,14, False)
	yield swap_positions(pos, 3,7,11,15, False)
	yield swap_positions(pos, 0,4,8,12, True)
	yield swap_positions(pos, 1,5,9,13, True)
	yield swap_positions(pos, 2,6,10,14, True)
	yield swap_positions(pos, 3,7,11,15, True)

if __name__ == "__main__":
	main()