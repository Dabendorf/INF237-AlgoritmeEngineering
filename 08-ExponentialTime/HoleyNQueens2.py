import sys
from collections import defaultdict

def main():
	while True:
		board_size, num_of_holes = list(map(int, sys.stdin.readline().strip().split(" ")))
		if board_size == 0 and num_of_holes == 0:
			exit(0)
		holes = defaultdict(lambda: set())
		for i in range(num_of_holes):
			# Reads one list of integers per line
			
			hole = [int(i) for i in sys.stdin.readline().strip().split(" ")]
			holes[hole[0]].add(hole[1])
		
		print(len(damenproblem(board_size, board_size, holes)))

def damenproblem(reihen, spalten, holes):
	if reihen <= 0:
		return [[]]
	else:
		num = eine_dame_dazu(reihen - 1, spalten, damenproblem(reihen - 1, spalten, holes), holes)
		return num

def eine_dame_dazu(neue_reihe, spalten, vorherige_loesungen, holes):
	neue_loesungen = []
	for loesung in vorherige_loesungen:
		for neue_spalte in range(spalten):
			if kein_konflikt(neue_reihe, neue_spalte, loesung, holes):
				neue_loesungen.append(loesung + [neue_spalte])
	return neue_loesungen

def kein_konflikt(neue_reihe, neue_spalte, loesung, holes):
	for reihe in range(neue_reihe):
		# col, row, diag or hole
		if loesung[reihe] == neue_spalte:
			return False
		if loesung[reihe] + reihe == neue_spalte + neue_reihe:
			return False
		if loesung[reihe] - reihe == neue_spalte - neue_reihe:
			return False
		if neue_reihe in holes[neue_spalte]:
			return False
	return True

if __name__ == "__main__":
	main()