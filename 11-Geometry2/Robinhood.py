import sys
import math

""" The task is to find the maximum distance of two points in a big number of points.

	Solution:
	- This makes use of the Graham Scan algorithm. 
	- One sorts all points by x-value (break tie by y-value)
	- Then we calculate both an upper hull and a lower hull both times through the same process
	- In the first one, we go through the sorted points and in the second one through the reversed order
	- We add all points to the hull with have certain properties.
	- We try to find out of three points are in a left angle
	which is the same as finding out if they are inner points or outside hull points
	- 
	"""
def main():
	num_of_points = int(sys.stdin.readline())

	# Reading of all points
	points = []
	for _ in range(num_of_points):
		case = [float(i) for i in sys.stdin.readline().strip().split(" ")]
		points.append((case[0], case[1]))

	# Calculating result
	print(robinhood(points))
		
def robinhood(points):
	# Sorting of all points by x value
	points = sorted(set(points))
	S, hull= [], []

	# Go through all points in that order
	# Pop upper elements of S if there are at least two of them and
	# if they are in left angle together with point p
	for p in points:
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	hull += S

	# Calculate the same in reversed order to get lower hull
	S = []
	for p in reversed(points):
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	hull += S

	# The maximum distance of two pairs of many points is the maximum distance of the points of the hull
	# Go through hull with two for-loops with points being on "opposite" position
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

def leftturn(p1, p2, p3):
	"""Helper method leftturn which calculates if three points are a left or a right angle """
	area = (p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) * (p3[1]-p2[1])
	return area < 0

if __name__ == "__main__":
	main()