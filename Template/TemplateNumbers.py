import sys
from collections import defaultdict

if len(sys.argv) > 2:
	debug = print
else:
	debug = lambda *_,**__:None

def main():
	num_of_cases = int(sys.stdin.readline())

	for line in sys.stdin:
		# Reads one Integer per line
		line = int(line.strip())
		

if __name__ == "__main__":
	main()