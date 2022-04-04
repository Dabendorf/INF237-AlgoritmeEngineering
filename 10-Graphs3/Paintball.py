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
	players, edges = list(map(int, sys.stdin.readline().strip().split()))

	# Read original graph into original capacities, every node exists two times as "a" and "b" (bipartite)
	orig_cap = list()
	for _ in range(edges):
		A, B = list(map(int, sys.stdin.readline().strip().split()))
		orig_cap.append((f"{A}a", f"{B}b", 1))
		orig_cap.append((f"{B}a", f"{A}b", 1))
		
	# Add s and t including edges to all of them
	V = list()
	for i in range(1, players+1):
		orig_cap.append(("s", f"{i}a", 1))
		orig_cap.append((f"{i}b", "t", 1))
		V.append(f"{i}a")
		V.append(f"{i}b")

	V.append("s")
	V.append("t")

	graph = Graph(orig_cap, V)
	s = "s"
	t = "t"

	"""for key, value in graph.R.items():
		print(key, dict(value))"""

	# Run max-flow
	mflow = maxflow(graph, s, t)

	"""for key, value in graph.R.items():
		print(key, dict(value))"""


	if mflow == players:
		output = [0] * players

		for fra, v in graph.edges.items():
			for til, weight in v.items():
				val_res = graph.R[til][fra]
				if val_res != 0 and fra != "s" and til != "t":
					output[int(fra[:-1])-1] = til[:-1]

		print("\n".join(output))
	else:
		print("Impossible")

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