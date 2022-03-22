import sys
from collections import defaultdict

if len(sys.argv) > 1:
	debug = print
else:
	debug = lambda *_,**__:None

def main():
	orig_positions = list()
	goal = [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3]
	letter_to_num = {"R":0, "G":1, "B":2, "Y":3}

	for i in range(4):
		line = [letter_to_num[i] for i in list(sys.stdin.readline().strip())]
		orig_positions.extend(line)

	debug(orig_positions)
	#for i in neighbours(orig_positions):

	print(bidirectional_search(orig_positions, goal))

def bidirectional_search(start, goal):
	visited_start = list()
	visited_end = list()
	parent_start = dict()
	parent_end = dict()

	queue_start = [start]
	queue_goal = [goal]

	visited_start.append(start)
	visited_end.append(goal)

	meeting_point = None # later used together with parent to find the depth

	while queue_start and queue_goal and meeting_point is None:
		s = queue_start.pop()
		for u in neighbours(s):
			print(f"neighbour u, visited: {len(visited_start)}")
			if not u in visited_start:
				queue_start.append(u)
				visited_start.append(u)
				parent_start[tuple(u)] = s

		if s == goal or s in queue_goal:
			return True

		t = queue_goal.pop()
		for v in neighbours(t):
			print(f"neighbour v, visited: {len(visited_end)}")
			if not v in visited_end:
				queue_goal.append(v)
				visited_end.append(v)
				parent_end[tuple(v)] = t

		if t == start or s in queue_start:
			return True


def bfs(s, adj_list):
	""" Its a BFS. The way a BFS always has behaved"""
	output_list = set()
	visited = defaultdict(lambda: False)

	# Queue starts with start node
	queue = [s]
	visited[s] = True

	# While queue, go through them
	while queue:
		s = queue.pop()

		if s != None:
			output_list.add(s)

		# Mark neighbours as visited and add to queue
		for i in adj_list[s]:
			if visited[i] == False:
				queue.append(i)
				visited[i] = True

	# Returns list of all visited nodes
	return output_list

def swap_positions(pos_old, a, b, c, d, left):
	pos = pos_old.copy()

	if left:
		swap = pos[a]
		pos[a] = pos[b]
		pos[b] = pos[c]
		pos[c] = pos[d]
		pos[d] = swap
	else:
		swap = pos[d]
		pos[d] = pos[c]
		pos[c] = pos[b]
		pos[b] = pos[a]
		pos[a] = swap
	return pos

def neighbours(orig_positions):
	pos = orig_positions.copy()
	yield swap_positions(pos, 0,1,2,3, False)
	yield swap_positions(pos, 4,5,6,7, False)
	yield swap_positions(pos, 8,9,10,11, False)
	yield swap_positions(pos, 12,13,14,15, False)
	yield swap_positions(pos, 0,1,2,3, True)
	yield swap_positions(pos, 4,5,6,7, True)
	yield swap_positions(pos, 8,9,10,11, True)
	yield swap_positions(pos, 12,13,14,15, True)
	yield swap_positions(pos, 0,4,8,12, False)
	yield swap_positions(pos, 1,5,9,13, False)
	yield swap_positions(pos, 2,6,10,14, False)
	yield swap_positions(pos, 3,7,11,15, False)
	yield swap_positions(pos, 0,4,8,12, True)
	yield swap_positions(pos, 1,5,9,13, True)
	yield swap_positions(pos, 2,6,10,14, True)
	yield swap_positions(pos, 3,7,11,15, True)

if __name__ == "__main__":
	main()