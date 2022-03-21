import sys
from collections import defaultdict

if len(sys.argv) > 1:
	debug = print
else:
	debug = lambda *_,**__:None

def main():
	line = sys.stdin.readline().strip()
	dices = [int(i) for i in line.split(" ")]
	
	count_dict = defaultdict(lambda: 0)
	count_dict[5] = 3
	for a in range(10):
		count_dict[a] += 1

	print(count_dict)
		

if __name__ == "__main__":
	main()