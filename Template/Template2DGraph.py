import sys
from collections import defaultdict

if len(sys.argv) > 2:
	debug = print
else:
	debug = lambda *_,**__:None

class Graph:
	nodes = []
	edges = defaultdict(lambda: [])

	def add_node(self, name: str):
		if name not in self.nodes:
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

def main():
	height, width = map(int, sys.stdin.readline().strip().split(" "))

	grid = []
	for _ in range(height):
        # Reads one list of integers per line
		#case_str = sys.stdin.readline().strip().split("")
		case_str = list(sys.stdin.readline().strip())
		print(case_str)
		#case = [int(i) for i in case_str]
		grid.append(case_str)

	g = Graph()
	for y in range(height):
		for x in range(width):
			g.add_node((x, y, grid[y][x]))

	for y in range(height):
		for x in range(width):
			g.add_node((x, y, grid[y][x]))
			if x < width-1:
				g.add_edge((x, y, grid[y][x]), (x+1, y, grid[y][x+1]))
			if y < height-1:
				g.add_edge((x, y, grid[y][x]), (x, y+1, grid[y+1][x]))

	print(grid)
	print(g.nodes)
	print(len(g.nodes))
	print(g.edges)
	print(len(g.edges))
		

if __name__ == "__main__":
	main()