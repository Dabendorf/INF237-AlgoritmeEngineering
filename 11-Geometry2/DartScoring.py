import sys
import math

""" The task is to find the length of the hull of a big number of points
	and then calculate a fancy point sum by a given formula.

	Solution:
	- This makes use of the Graham Scan algorithm. 
	- One sorts all points by x-value (break tie by y-value)
	- Then we calculate both an upper hull and a lower hull both times through the same process
	- In the first one, we go through the sorted points and in the second one through the reversed order
	- We add all points to the hull with have certain properties.
	- We try to find out of three points are in a left angle
	which is the same as finding out if they are inner points or outside hull points
	- Finally, we calculate the length of the hull by going around the hull and add distances and put them into the formula
	- This is possible since Graham scan adds points to the hull in order
	"""
def main():
	# One line is one test case
	for line in sys.stdin:
		case = [float(i) for i in line.strip().split(" ")]
		
		len_case = len(case)//2
		points = []

		# Splitting the points into two parts (since its pairs of x y)
		for i in range(len_case):
			points.append((case[2*i], case[2*i+1]))

		# Calculates the length of the hull
		hulllen = graham(points)

		# Calculates final output
		output = 100*len(points)/(1+hulllen)
		print(output)
		
def graham(points):
	# Sorting of all points by x value
	points = sorted(set(points))
	S, hull1, hull2 = [], [], []

	# Go through all points in that order
	# Pop upper elements of S if there are at least two of them and
	# if they are in left angle together with point p
	for p in points:
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	
	# Add all points left to the hull
	hull1 += S

	# Calculate the same in reversed order to get lower hull
	S = []
	for p in reversed(points):
		while len(S) >= 2 and leftturn(S[-2], S[-1], p):
			S.pop()
		S.append(p)
	hull2 += S

	# Call hulllength for both upper and lower hull
	return hulllength(hull1) + hulllength(hull2)

def leftturn(p1, p2, p3):
	"""Helper method leftturn which calculates if three points are a left or a right angle """
	area = (p2[1]-p1[1]) * (p3[0]-p2[0]) - (p2[0]-p1[0]) * (p3[1]-p2[1])
	return area < 0

def hulllength(hull):
	"""Helper method calculating the length of the hull by going around and adding distances"""
	sum = 0
	for i in range(1,len(hull)):
		p1 = hull[i]
		p2 = hull[i-1]
		sum += math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)
	return sum

if __name__ == "__main__":
	main()