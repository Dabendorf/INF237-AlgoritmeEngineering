// https://open.kattis.com/problems/citrusintern

import java.util.ArrayList;
import java.util.Collections;
import java.util.Set;
import java.util.Stack;
import java.util.TreeSet;

/**
 * A companies structure is built up like a tree with every person having up to one boss and several subordinates
 * We want every person in the company to be controlled by either being bribed or having a "talk" to a bribe boss or subordinate
 * Every bribed person talks to his/her boss and the subordinates
 * No two people talking with each other should be bribed at the same time and the money spend on bribery should be minimised
 * 
 * Indendent Set & Dominating Set, see INF234 weighted independent set on trees
 * 
 * Solution:
 * - First: Find the root node and the postorder of the tree structure.
 * - Finding root: Start at the leafes and go up until one does not have a boss anymore
 * - Postorder: Using DFS, returning a stack of postorder. This way, one can start dynamic programming at the leafes going up
 * 
 * - Now, its a dynamic programming problem. There are three 1D-lists being:
 * - m_bribe[u]: The money spent until u if u gets bribed
 * - m_notbribed[u]: The money spent until u if u is not bribed
 * - m_notbribed_butchild[u]: The money spent until u if u is not bribed but at least one of the child
 * - The latter one is relevant such that there is no hole in the tree where one person is not bribed
 * 
 * - Base case: For every leaf u: m_bribed[u] = m_notbribed_butchild[u] = w_u; m_notbribed[u] = 0
 * - Recurrance:
 * - m_bribed[u] = sum of all neighbours v not being bribed + bribing money of u
 * - m_notbribed[u] = sum of all neighbours v with value of the minimum of v being bribed or a child of v behind bribed
 * - m_notbribed_butchild[u] = minimum bribing value of neighbour which is sum of not bribing u but bribing v + the minimum of bribing v or not bribing v but its children
 * - It is basically not taking u and then calculating which child to take
 * - The best child is that one which has minimum cost of taking it, it is a merging of branches
 * 
 * - The final output is the minimum of bribing v or one of its children
 */
public class CitrusIntern {
	public static void main(String[] args) {
		Kattio io = new Kattio(System.in, System.out);

		// Reading cases
		int numOfPeople = io.getInt();
		int[] bribe = new int[numOfPeople];
		ArrayList<Set<Integer>> subordinates = new ArrayList<Set<Integer>>();
		Set<Integer> leafs = new TreeSet<>();

		int[] bosses = new int[numOfPeople];
		for(int i=0; i<numOfPeople; i++) {
			bosses[i] = -1;
		}

		// Initialise two datastructures
		// An array of bribery sums
		// An ArrayList of Sets telling about the subordinates of every person
		for(int i=0; i<numOfPeople; i++) {
			bribe[i] = io.getInt();
			int numOfSubordinates = io.getInt();
			
			subordinates.add(new TreeSet<Integer>());
			for(int j=0; j<numOfSubordinates; j++) {
				int subOrdNum = io.getInt();
				subordinates.get(i).add(subOrdNum);
				bosses[subOrdNum] = i;
			}
			if(numOfSubordinates==0) {
				leafs.add(i);
			}
		}

		// Initialise three new arrays
		// m_bribe: The person gets bribed
		// m_notbribe: The person does not get bribed
		// m_notbribe_butchild: The person does not get bribed, but at least one child is (which is a condition)

		long[] m_bribe = new long[numOfPeople];
		long[] m_notbribe = new long[numOfPeople];
		long[] m_notbribe_butchild = new long[numOfPeople];

		// Base Cases, leafs
		for(int personIndex = 0; personIndex<numOfPeople; personIndex++) {
			if(subordinates.get(personIndex).size()==0) {
				m_bribe[personIndex] = bribe[personIndex];
				m_notbribe[personIndex] = 0L;
				m_notbribe_butchild[personIndex] = bribe[personIndex];
			}
		}

		// Find the root of the tree and then the postorder, starting with leafs and then going up
		int root = findRoot(bosses, numOfPeople, leafs);
		Stack<Integer> postorder = dfs_postorder(subordinates, numOfPeople, root);

		// Dynamic programming algorithm itself
		while(postorder.size() > 0) {
			//traversing through postorder
			int u = postorder.pop();

			if(leafs.contains(u)) {
				continue;
			}
			// Calculate m_bribe if we bribe u
			// Sum of all child v when they arent bribed + bribing money of u itself
			long sum = bribe[u];
			for(int v: subordinates.get(u)) {
				sum += m_notbribe[v];
			}
			m_bribe[u] = sum;

			// Calculate m_notbribe if we dont bribe u
			// Sum of minimum of every childs bribe and "child bribed" array
			sum = 0;
			for(int v: subordinates.get(u)) {
				sum += Math.min(m_bribe[v], m_notbribe_butchild[v]);
			}
			m_notbribe[u] = sum;

			// Calculate m_notbribe_butchild if we dont bribe u but one of the child got bribed
			// The minimum bribing value of neighbour which is sum of not bribing u but bribing v
			// + the minimum of bribing v or not bribing v but its children
			ArrayList<Long> neighbourbribes = new ArrayList<Long>();
			for(int v: subordinates.get(u)) {
				long temp = m_bribe[v] - Math.min(m_bribe[v], m_notbribe_butchild[v]);
				neighbourbribes.add(temp);
			}
			m_notbribe_butchild[u] = m_notbribe[u] + Collections.min(neighbourbribes);

			/*System.out.println(u);
			System.out.println(Arrays.toString(m_bribe));
			System.out.println(Arrays.toString(m_notbribe));
			System.out.println(Arrays.toString(m_notbribe_butchild));*/
		}

		System.out.println(Math.min(m_bribe[root], m_notbribe_butchild[root]));
		io.close();
	}

	/**
	 * Function aims to find the root of the tree
	 * It takes as argument all leafs and then iterates up until it finds a node without a parent
	 * @param bosses Array which number is the boss of which person
	 * @param numOfNodes Number of all people
	 * @param leafs List of initial leafs
	 * @return Root note number
	 */
	static int findRoot(int[] bosses, int numOfNodes, Set<Integer> leafs) {
		Stack<Integer> nextLeafs = new Stack<>();
		for(int leaf: leafs) {
			nextLeafs.push(leaf);
		}

		while(nextLeafs.size() > 0) {
			int s = nextLeafs.pop();
			int bossOfS = bosses[s];
			if(bossOfS == -1) {
				return s;
			} else {
				nextLeafs.push(bossOfS);
			}
		}

		// should not happen, error case
		return -2;
	}

	/**
	 * Goes through the tree to find the postorder of it
	 * @param adjList List of subordinates for each person
	 * @param numOfNodes Number of people
	 * @param startNode Root note
	 * @return Stack for postorder traversel
	 */
	static Stack<Integer> dfs_postorder(ArrayList<Set<Integer>> adjList, int numOfNodes, int startNode) {
		boolean[] visited = new boolean[numOfNodes];

		for(int i=0; i<numOfNodes; i++) {
			visited[i] = false;
		}

		Stack<Integer> nextNodes = new Stack<>();
		Stack<Integer> postorder = new Stack<>();

		nextNodes.push(startNode);

		while(!nextNodes.empty()) {
			int s = nextNodes.pop();
			postorder.push(s);

			if(!visited[s]) {
				visited[s] = true;
			}

			for(int t: adjList.get(s)) {
				if(!visited[t]) {
					nextNodes.push(t);
				}
			}
		}
		return postorder;
	}

}