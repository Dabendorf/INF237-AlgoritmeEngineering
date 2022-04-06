import sys
from typing import Tuple
from collections import defaultdict, deque

class Graph:
	edges = defaultdict(lambda: defaultdict(lambda: None))
	R = defaultdict(lambda: defaultdict(lambda: 0))

	def __init__(self, orig_cap, V):
		for k in orig_cap:
			a,b,w = k
			self.edges[a][b] = w
			self.R[a][b] = w
		self.V = V

def main():
	num_pedestals, num_vases = list(map(int, sys.stdin.readline().strip().split()))

	ped_diam = list()
	for i in range(num_pedestals):
		a, b = list(map(int, sys.stdin.readline().strip().split()))
		ped_diam.append((a, b))
	vases_diam = list(map(int, sys.stdin.readline().strip().split()))

	orig_cap = list()
	V = ["s", "t"]
	for idx_v, v in enumerate(vases_diam):
		orig_cap.append(("s", "v"+str(idx_v+1), 1))
		V.append("v"+str(idx_v+1))
		for idx_p, p in enumerate(ped_diam):
			if v == p[0] or v == p[1]:
				orig_cap.append(("v"+str(idx_v+1), "p"+str(idx_p+1), 1))

	for idx_p, p in enumerate(ped_diam):
		orig_cap.append(("p"+str(idx_p+1), "t", 1))
		V.append("p"+str(idx_p+1))

	graph = Graph(orig_cap, V)
	s = "s"
	t = "t"

	maxflow(graph, s, t)
	solutions = list()
	for fra, v in graph.edges.items():
		for til, weight in v.items():
			val_res = graph.R[til][fra]
			if val_res != 0 and fra != "s" and til != "t":
				solutions.append(til[1:])

	if len(solutions) == num_vases:
		for el in solutions:
			print(el)
	else:
		print("impossible")

edges = lambda p: zip(p, p[1:])

def bfs(graph, s, t):
	q = deque([s])
	parent = {}
	while q:
		v = q.popleft()
		for u in graph.R[v]: # !
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
