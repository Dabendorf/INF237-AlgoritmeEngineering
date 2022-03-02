from collections import defaultdict
import sys
from collections import deque

class Graph:
	V = ["s", "a", "b", "c", "d", "e", "f", "g", "t"]
	edges = defaultdict(lambda: defaultdict(lambda: None))
	R = defaultdict(lambda: defaultdict(lambda: 0))

	def __init__(self):
		orig_cap = [('a', 's', 1), ('s', 'b', 5), ('s', 'c', 5), ('b', 'a', 3), ('a', 'd', 3),
			('d', 'b', 1), ('b', 'e', 2), ('c', 'b', 1), ('e', 'c', 1), ('c', 'f', 5), 
			('d', 'e', 3), ('d', 't', 2), ('e', 't', 3), ('f', 'e', 1), ('f', 'g', 5), 
			('g', 't', 5)]

		for k in orig_cap:
			a,b,w = k
			self.edges[a][b] = w
			self.R[a][b] = w

def main():
	graph = Graph()
	s = "s"
	t = "t"

	print(maxflow(graph, s, t))

	for fra, v in graph.edges.items():
		for til, weight in v.items():
			val_res = graph.R[til][fra]
			if val_res != 0:
				print(fra, til, val_res)

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
	while P := bfs(graph, s, t):
		F = min(graph.R[v][u] for (v, u) in edges(P))
		flow += F
		for i in range(1, len(P)):
			v, u = P[i - 1], P[i]
			graph.R[v][u] -= F
			graph.R[u][v] += F
	return flow

if __name__ == "__main__":
	main()