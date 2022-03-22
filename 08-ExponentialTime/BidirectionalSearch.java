import java.util.*;

class BidirectionalSearch {
	static String BidirectionalSearchPath(Graph G, int src, int dest) {
		String path = "";
		boolean[] Visited1 = new boolean[G.V];
		boolean[] Visited2 = new boolean[G.V];
		int[] parent1 = new int[G.V];
		int[] parent2 = new int[G.V];
		for (int i = 0; i < G.V; i++) {
			Visited1[i] = false;
			Visited2[i] = false;
			parent1[i] = -1;
			parent2[i] = -1;
		}
		ArrayList<Integer> queue1 = new ArrayList<>();
		ArrayList<Integer> queue2 = new ArrayList<>();
		queue1.add(src);
		Visited1[src] = true;
		queue2.add(dest);
		Visited2[dest] = true;
		int intersection = -1;
		while (queue1.size() > 0 && queue2.size() > 0 && intersection == -1) {
			G.BFS(queue1, Visited1, parent1);
			G.BFS(queue2, Visited2, parent2);

			for (int i = 0; i < G.V; i++) {
				if (Visited1[i] && Visited2[i]) { // checking intersection
					intersection = i;
					break;
				}
			}
		}

		if (intersection == -1)
			return "";

		String path1 = "";
		int j = intersection;
		while (j != -1) {
			path1 = j + " " + path1;
			j = parent1[j];
		}
		String path2 = "";
		j = parent2[intersection];
		while (j != -1) {
			path2 = path2 + j + " ";
			j = parent2[j];
		}
		path = path1 + path2;
		return path;
	}

	public static void main(String[] args) {
		Scanner inp = new Scanner(System.in);
		System.out.println("Enter the number of vertices");
		int v = inp.nextInt();
		System.out.println("Enter the number of edges");
		int e = inp.nextInt();
		Graph G = new Graph(v, e);
		System.out.println("Edges:");
		for (int i = 0; i < G.E; i++) {
			int x = inp.nextInt();
			int y = inp.nextInt();
			G.add_edge(x, y);
		}
		String path = BidirectionalSearchPath(G, 0, 2);
		if (path.equals(""))
			System.out.println("Path does not exist");
		else
			System.out.println("Path : " + path);
		inp.close();
	}
}