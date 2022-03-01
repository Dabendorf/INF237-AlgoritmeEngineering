from collections import defaultdict
import sys
#from networkx.exception import NetworkXError, NetworkXNoPath
#import numpy as np
#import networkx as nx
import pprint as pp

def main():
	#G_orig = nx.DiGraph()
	#G = nx.DiGraph()
	#G_f = nx.DiGraph()
	G_orig = defaultdict(lambda: [])
	G = defaultdict(lambda: [])
	G_f = defaultdict(lambda: [])

	# Insert original capacities in here
	orig_cap = [('a', 's', 1), ('s', 'b', 5), ('s', 'c', 5), ('b', 'a', 3), ('a', 'd', 3),
	('d', 'b', 1), ('b', 'e', 2), ('c', 'b', 1), ('e', 'c', 1), ('c', 'f', 5), 
	('d', 'e', 3), ('d', 't', 2), ('e', 't', 3), ('f', 'e', 1), ('f', 'g', 5), 
	('g', 't', 5)]
	# orig_cap = [('s', 'a', 50), ('s', 'b', 50), ('a', 't', 1), ('b', 't', 2), ('a', 'b', 1)]
	
	num_of_nodes = len(orig_cap)
	for el in orig_cap:
		fra, til, weight = el
		G_orig[fra].append((til, weight))
		G[fra].append((til, 0))
		G_f[fra].append((til, weight))

	print(bfs("s", G_orig, num_of_nodes, "t"))
	exit(0)

	shortest_path = None
	try:
		shortest_path = nx.shortest_path(G_f, 's', 't')
	except NetworkXNoPath:
		shortest_path = None

	counter = 0
	while shortest_path != None:
		try:
			shortest_path = nx.shortest_path(G_f, 's', 't')
		except NetworkXNoPath:
			shortest_path = None
		
		if shortest_path != None:
			edge_lenghts = []
			for edge_ind in range(len(shortest_path)-1):
				edge_lenghts.append(G_f.get_edge_data(shortest_path[edge_ind], shortest_path[edge_ind+1])["weight"])
			min_edge_length = min(edge_lenghts)

			# Set edge sizes in flow graph
			for edge_ind in range(len(shortest_path)-1):
				# If G has that Node, increase size by min_edge_length
				if G.has_edge(shortest_path[edge_ind], shortest_path[edge_ind+1]):
					G[shortest_path[edge_ind]][shortest_path[edge_ind+1]]['weight'] += min_edge_length
				else:
					# If G doesn't have it:
					# Check if original G had it and set it to this size
					# (thats the case if edge was empty for some time)
					if G_orig.has_edge(shortest_path[edge_ind], shortest_path[edge_ind+1]):
						G.add_edge(shortest_path[edge_ind], shortest_path[edge_ind+1], weight= min_edge_length)
					else:
						# Otherwise its a backwards edge, substract value from edge in other direction
						G[shortest_path[edge_ind+1]][shortest_path[edge_ind]]['weight'] -= min_edge_length

				# Decrease edge capacity in residential graph
				G_f[shortest_path[edge_ind]][shortest_path[edge_ind+1]]['weight'] -= min_edge_length

				# If that edge now is zero in residential graph, delete it
				if G_f[shortest_path[edge_ind]][shortest_path[edge_ind+1]]['weight'] == 0:
					G_f.remove_edge(shortest_path[edge_ind], shortest_path[edge_ind+1])
				
				# If G_f has backwards edge, add min_edge-length to it, if not create edge
				if G_f.has_edge(shortest_path[edge_ind+1], shortest_path[edge_ind]):
					G_f[shortest_path[edge_ind+1]][shortest_path[edge_ind]]['weight'] += min_edge_length
				else:
					G_f.add_edge(shortest_path[edge_ind+1], shortest_path[edge_ind], weight=min_edge_length)

				# If that edge now is zero in residential graph, delete it
				if G_f[shortest_path[edge_ind+1]][shortest_path[edge_ind]]['weight'] == 0:
					G_f.remove_edge(shortest_path[edge_ind+1], shortest_path[edge_ind])
		
			print("Iteration")
			print(shortest_path)
			pp.pprint(list(G.edges(data=True)))
			print("Outgoing flow: "+str(G.out_degree('s', weight="weight")))
			print("Ingoing flow: "+str(G.in_degree('t', weight="weight")))
			print("=============")
			
	print("Finished")
	print("Output flow")
	pp.pprint(list(G.edges(data=True)))
	print("Outgoing flow: "+str(G.out_degree('s', weight="weight")))
	print("Ingoing flow: "+str(G.in_degree('t', weight="weight")))
	print("Residential graph")
	pp.pprint(list(G_f.edges(data=True)))
	print("Min-cut: "+str(list(nx.dfs_postorder_nodes(G_f, 's'))))

def bfs(s, adj_list, num_of_nodes, end):
	""" Its a BFS. The way a BFS always has behaved"""

	# Queue starts with start node
	queue = [s]
	visitedFrom = defaultdict(lambda: None)#[None] * num_of_nodes

	# While queue, go through them
	while queue:
		s = queue.pop()

		# Mark neighbours as visited and add to queue
		for i in adj_list[s]:
			if visitedFrom[i[0]] == None:
				queue.append(i[0])
				visitedFrom[i[0]] = s

	curr = end
	output = [end]

	while curr != s:
		curr = visitedFrom[curr]
		output.append(curr)
	return output[::-1]

if __name__ == "__main__":
	main()