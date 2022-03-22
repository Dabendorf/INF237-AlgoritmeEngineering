
// Part of OpenGenus
import java.util.*;

class Graph {
	int V; // Number of veritces
	int E; // Number of edges
	ArrayList<Integer>[] Adj; // adjacency list

	Graph(int v, int e) {
		V = v;
		E = e;
		Adj = new ArrayList[V];
		for (int i = 0; i < V; i++) {
			Adj[i] = new ArrayList<Integer>();
		}
	}

	void add_edge(int src, int dest) {
		Adj[src].add(dest);
		Adj[dest].add(src);
	}

	void BFS(ArrayList<Integer> queue, boolean[] visited, int[] parent) {
		int current = queue.remove(0);
		for (int i = 0; i < Adj[current].size(); i++) {
			int x = Adj[current].get(i);
			if (!visited[x]) {
				queue.add(x);
				visited[x] = true;
				parent[x] = current;
			}
		}
	}
}

