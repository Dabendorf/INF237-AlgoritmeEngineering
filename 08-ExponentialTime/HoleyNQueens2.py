import sys
from typing import Tuple
from collections import defaultdict
from itertools import permutations

def main():
	board_size, num_of_holes = list(map(int, sys.stdin.readline().strip().split(" ")))

	holes = defaultdict(lambda: set())
	for i in range(num_of_holes):
		# Reads one list of integers per line
		
		hole = [int(i) for i in sys.stdin.readline().strip().split(" ")]
		#holes.add((hole[0], hole[1]))
		holes[hole[0]].add(hole[1])
	
	print(len(damenproblem(board_size, board_size, holes)))
	print(holes)

def damenproblem(reihen, spalten, holes):
	if reihen <= 0:
		return [[]] # keine Dame zu setzen; leeres Brett ist Lösung
	else:
		print(f"Neue Dame dazu: Reihe {reihen-1}")
		num = eine_dame_dazu(reihen - 1, spalten, damenproblem(reihen - 1, spalten, holes), holes)
		print(num)
		return num

# Probiere alle Spalten, in denen für eine gegebene Teillösung
# eine Dame in "neue_reihe" gestellt werden kann.
# Wenn kein Konflikt mit der Teillösung auftritt,
# ist eine neue Lösung des um eine Reihe erweiterten
# Bretts gefunden.
def eine_dame_dazu(neue_reihe, spalten, vorherige_loesungen, holes):
	print(f"Neue Reihe: {neue_reihe}")
	neue_loesungen = []
	for loesung in vorherige_loesungen:
		# Versuche, eine Dame in jeder Spalte von neue_reihe einzufügen.
		for neue_spalte in range(spalten):
			#print(neue_spalte, neue_reihe)
			# print('Versuch: %s in Reihe %s' % (neue_spalte, neue_reihe))
			if kein_konflikt(neue_reihe, neue_spalte, loesung, holes):
				# Kein Konflikte, also ist dieser Versuch eine Lösung.
				neue_loesungen.append(loesung + [neue_spalte])
	return neue_loesungen

# Kann eine Dame an die Position "neue_spalte"/"neue_reihe" gestellt werden,
# ohne dass sie eine der schon stehenden Damen schlagen kann?
def kein_konflikt(neue_reihe, neue_spalte, loesung, holes):
	for reihe in range(neue_reihe):
		if (loesung[reihe]         == neue_spalte              or  # gleiche Spalte
			loesung[reihe] + reihe == neue_spalte + neue_reihe or  # gleiche Diagonale
			loesung[reihe] - reihe == neue_spalte - neue_reihe):   # gleiche Diagonale
				return False
		if neue_reihe in holes[neue_spalte]:
			return False
	return True

if __name__ == "__main__":
	main()