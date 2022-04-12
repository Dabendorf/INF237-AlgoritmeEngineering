import sys
import math
from collections import defaultdict

def main():
	num_of_points = int(sys.stdin.readline())

	points = []
	for _ in range(num_of_points):
		case = [float(i) for i in sys.stdin.readline().strip().split(" ")]
		
		
		points.append((case[0], case[1]))
	#print(points)
	print(robinhood(points))
		
def robinhood(points):
	points = sorted(set(points))
	S, hull= [], [] # S is a stack of points

	for p in points:
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	hull += S

	S = []
	for p in reversed(points):
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	hull += S[1:-1]

	maxdis = 0
	currdis = 0
	for i in range(len(hull)):
		p1 = hull[i]
		for j in range(len(hull)):
			p2 = hull[(i+j)%len(hull)]
			dis = math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)
			if currdis>dis:
				currdis = 0
				break
			currdis = dis

			if dis>maxdis:
				maxdis = dis

		
		return maxdis

	#print(f"{}")
	#print(hull1)
	#print(hull2)

def leftturn(p1, p2, p3):
	area = (p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) * (p3[1]-p2[1])
	return area < 0

if __name__ == "__main__":
	main()