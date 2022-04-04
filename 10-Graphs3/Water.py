# https://open.kattis.com/problems/water

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
	num_stations, num_pipes, num_improvements = list(map(int, sys.stdin.readline().strip().split()))

	# Read original graph into original capacities, every node exists two times as "a" and "b" (bipartite)
	orig_cap = list()
	for _ in range(num_pipes):
		A, B, weight = list(map(int, sys.stdin.readline().strip().split()))
		orig_cap.append((A, B, weight))
		orig_cap.append((B, A, weight))

	V = list(range(1, num_stations+1))

	graph = Graph(orig_cap, V)
	s = 1
	t = 2

	# Run max-flow
	mflow = maxflow(graph, s, t)
	print(mflow)

	for _ in range(num_improvements):
		A, B, weight = list(map(int, sys.stdin.readline().strip().split()))

		if graph.edges[A][B] != None:
			graph.edges[A][B] += weight
			graph.edges[B][A] += weight
			graph.R[A][B] += weight
			graph.R[B][A] += weight
		else:
			graph.edges[A][B] = weight
			graph.edges[B][A] = weight
			graph.R[A][B] = weight
			graph.R[B][A] = weight

		maxflow_new = maxflow(graph, s, t) + mflow
		mflow = maxflow_new
		print(mflow)

edges = lambda p: zip(p, p[1:])

def bfs(graph, s, t):
	q = deque([s])
	parent = {}
	while q:
		v = q.popleft()
		#for u in graph.V: # !
		for u in graph.R[v]:
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