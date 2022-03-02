import sys
from networkx.exception import NetworkXError, NetworkXNoPath
import numpy as np
import networkx as nx
import pprint as pp

# python FordFulkerson.py
def main():
	G_orig = nx.DiGraph()
	G = nx.DiGraph()
	G_f = nx.DiGraph()

	# Insert original capacities in here
	orig_cap = [('a', 's', 1), ('s', 'b', 5), ('s', 'c', 5), ('b', 'a', 3), ('a', 'd', 3),
	('d', 'b', 1), ('b', 'e', 2), ('c', 'b', 1), ('e', 'c', 1), ('c', 'f', 5), 
	('d', 'e', 3), ('d', 't', 2), ('e', 't', 3), ('f', 'e', 1), ('f', 'g', 5), 
	('g', 't', 5)]
	# orig_cap = [('s', 'a', 50), ('s', 'b', 50), ('a', 't', 1), ('b', 't', 2), ('a', 'b', 1)]

	G_orig.add_weighted_edges_from(orig_cap)
	G.add_weighted_edges_from(orig_cap)
	G_f.add_weighted_edges_from(orig_cap)

	for u,v,a in G.edges(data=True):
		G[u][v]['weight'] = 0

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
				#print(shortest_path[edge_ind], shortest_path[edge_ind+1])
				edge_lenghts.append(G_f.get_edge_data(shortest_path[edge_ind], shortest_path[edge_ind+1])["weight"])
				#print(G_f.get_edge_data(shortest_path[edge_ind], shortest_path[edge_ind+1])["weight"])
			#exit(0)
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


if __name__ == "__main__":
	main()