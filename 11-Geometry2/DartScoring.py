import sys
import math
from collections import defaultdict

def main():
	#num_of_cases = int(sys.stdin.readline())

	for line in sys.stdin:
		# Reads one list of integers per line
		case = [float(i) for i in line.strip().split(" ")]
		
		len_case = len(case)//2
		points = []
		for i in range(len_case):
			points.append((case[2*i], case[2*i+1]))
		#print("=====")
		hulllen = graham(points)
		output = 100*len(points)/(1+hulllen)
		print(output)
		
def graham(points):
	points = sorted(set(points))
	S, hull1, hull2 = [], [], [] # S is a stack of points

	for p in points:
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	hull1 += S

	S = []
	for p in reversed(points):
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	hull2 += S#[1:-1]

	#print(f"{}")
	#print(hull1)
	#print(hull2)

	return hulllength(hull1) + hulllength(hull2)

def leftturn(p1, p2, p3):
	area = (p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) * (p3[1]-p2[1])
	return area < 0

def hulllength(hull):
	sum = 0
	for i in range(1,len(hull)):
		p1 = hull[i]
		p2 = hull[i-1]
		sum += math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)
		#sum = sum + math.sqrt((hull[i-1][0]-hull[i][0])*(hull[i-1][0]-hull[i][0])+(hull[i-1][1]-hull[i][1])+(hull[i-1][1]-hull[i][1]))
	return sum
if __name__ == "__main__":
	main()