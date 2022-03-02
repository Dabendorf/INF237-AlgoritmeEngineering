import sys
from typing import Tuple
from collections import defaultdict

def main():
	tall = int(sys.stdin.readline().strip())

	if tall % 2 == 0:
		print("Alice\n1")
	else:
		print("Bob")
		

if __name__ == "__main__":
	main()