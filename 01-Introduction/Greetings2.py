# https://uib.kattis.com/problems/greetings2

import sys
from typing import Tuple
from collections import defaultdict

def main():
	line = sys.stdin.readline().strip()
	count = line.count('e')
	print("h"+(2*count*"e")+"y")
		

if __name__ == "__main__":
	main()