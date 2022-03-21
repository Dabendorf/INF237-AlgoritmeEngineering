import sys
from collections import defaultdict

if len(sys.argv) > 1:
	debug = print
else:
	debug = lambda *_,**__:None
class Graph:
	nodes = []
	edges = defaultdict(lambda: [])

	def add_node(self, name: str):
		self.nodes.append(name)
		self.edges[name] = []

	def add_nodes(self, names):
		self.nodes.extend(names)

	def add_edge(self, a: str, b: str, weight: int = 1, bidirected = True):
		if a not in self.nodes:
			self.nodes.append(a)
		if b not in self.nodes:
			self.nodes.append(b)

		self.edges[a].append(b)
		
		if bidirected:
			self.edges[b].append(a)

	def remove_edge(self, a: str, b: str, bidirected = True):
		self.edges[a].remove(b)

		if bidirected:
			self.edges[b].remove(a)

	def deg(self, node: str):
		return len(self.edges[node])

	def bfs(self, s):
		queue = [s] # queue with start node in it
		visited = []
		visited.append(s) # add first node as visited

		while len(queue) != 0:
			node = queue.pop(0) # take next queue node

			neighbours = self.edges[node]
			for neighbour in neighbours: # go through all neighbours, append nonvisited ones
				if neighbour not in visited:
					queue.append(neighbour)
					visited.append(neighbour)

		return visited # returns all found nodes

	# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
	def dfs(self, s, visited):
		if s not in visited:
			visited.append(s)

			neighbours = self.edges[s]
			for neighbour in neighbours:
				self.dfs(neighbour, visited)
		return visited


def main():
	num_of_cases = sys.stdin.readline()

	g = Graph()

	for line in sys.stdin:
		# Reads one list of integers per line
		#edge_str = line.strip().split(" ")
		#edge = [int(i) for i in edge_str]
		edge = line.strip().split(" ")
		g.add_edge(edge[0], edge[1])


	print(g.nodes)
	print(g.edges)

	print("BFS")
	print(g.bfs("A"))
	print("DFS")
	print(g.dfs("C", []))
		

if __name__ == "__main__":
	main()