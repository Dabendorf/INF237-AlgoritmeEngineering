# https://open.kattis.com/problems/pianolessons

from collections import defaultdict, deque
from sys import stdin

class Graph:
	edges = defaultdict(lambda: defaultdict(lambda: None))
	R = defaultdict(lambda: defaultdict(lambda: 0))

	def __init__(self, edges, R):
		self.edges = edges
		self.R = R

""" There are people wanting to take piano lessons and each has n time slots working for them.
	Each timeslot only accepts one student.
	Find the maximum number of students who can get piano lessons

	Solution:
	- Bipartite matching via flow networks
	- The people are set A and the piano lessons set B
	- Connect one set with a new node called "s" and one with a new node called "t"
	- Run Ford-Fulkerson (Edmonds-Karp) from "s" to "t"
	- Then go through all original edges and look if the opposite edge exists in the residual graph
	- If so it means that this is an edge in the bipartite matching
	- Output the maximum flow
	"""
def main():
	students, timeslots = list(map(int, stdin.readline().strip().split()))

	edges = defaultdict(lambda: defaultdict(lambda: None))
	R = defaultdict(lambda: defaultdict(lambda: 0))

	for idx_student in range(students):
		student_inf = list(map(int, stdin.readline().strip().split()))
		num_of_lessons = student_inf[0]

		if num_of_lessons > 0:
			for i in range(1, len(student_inf)):
				edges[idx_student+1][-student_inf[i]] = 1
				R[idx_student+1][-student_inf[i]] = 1
			
			edges["s"][idx_student+1] = 1
			R["s"][idx_student+1] = 1

	for idx_timeslots in range(timeslots):
		edges[-idx_timeslots-1]["t"] = 1
		R[-idx_timeslots-1]["t"] = 1

	graph = Graph(edges, R)

	mflow = maxflow(graph, "s", "t")

	print(mflow)

edges = lambda p: zip(p, p[1:])

def bfs(graph, s, t):
	q = deque([s])
	parent = {}
	while q:
		v = q.popleft()
		for u in graph.R[v]:
			if u in parent:
				continue
			if graph.R[v][u] <= 0:
				continue 
			parent[u] = v
			q.append(u)
			if u == t:
				return create_path(parent, s, t)

def create_path(parent, s, t):
	path = [t]
	while t != s:
		t = parent[t]
		path = [t] + path
	return tuple(path)

def maxflow(graph, s, t):
	flow = 0
	P = bfs(graph, s, t)
	while P:
		F = min(graph.R[v][u] for (v, u) in edges(P))
		flow += F
		for i in range(1, len(P)):
			v, u = P[i - 1], P[i]
			graph.R[v][u] -= F
			graph.R[u][v] += F
		P = bfs(graph, s, t)
	return flow

if __name__ == "__main__":
	main()