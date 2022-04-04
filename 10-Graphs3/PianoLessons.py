# https://open.kattis.com/problems/pianolessons

# https://open.kattis.com/problems/paintball

from collections import defaultdict, deque
import sys

class Graph:
	edges = defaultdict(lambda: defaultdict(lambda: None))
	R = defaultdict(lambda: defaultdict(lambda: 0))

	def __init__(self, orig_cap, V):
		for k in orig_cap:
			a, b, w = k
			self.edges[a][b] = w
			self.R[a][b] = w
		self.V = V

def main():
	students, timeslots = list(map(int, sys.stdin.readline().strip().split()))

	# Read original graph into original capacities, every node exists two times as "a" and "b" (bipartite)
	orig_cap = list()
	V = list()

	for idx_student in range(students):
		student_inf = list(map(int, sys.stdin.readline().strip().split()))
		num_of_lessons = student_inf[0]

		if num_of_lessons > 0:
			for i in range(1, len(student_inf)):
				orig_cap.append((idx_student, -student_inf, 1))
			
			orig_cap.append(("s", idx_student, 1))
			V.append(idx_student)

	for idx_timeslots in range(timeslots):
		orig_cap.append((-idx_timeslots, "t", 1))
		V.append(-idx_timeslots)

	V.append("s")
	V.append("t")

	#print(V)
	#print(orig_cap)

	graph = Graph(orig_cap, V)
	s = "s"
	t = "t"

	# Run max-flow
	mflow = maxflow(graph, s, t)

	print(mflow)

edges = lambda p: zip(p, p[1:])

def bfs(graph, s, t):
	q = deque([s])
	parent = {}
	while q:
		v = q.popleft()
		for u in graph.V: # !
			if u in parent:
				continue # seen it before
			if graph.R[v][u] <= 0:
				continue # vu saturated
			parent[u] = v
			q.append(u)
			if u == t:
				return create_path(parent, s, t)

def create_path(parent, s, t):
	path = [t]
	while t != s:
		t = parent[t]
		path.append(t)
	return tuple(reversed(path))

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