// https://open.kattis.com/problems/citrusintern

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.Stack;
import java.util.TreeSet;

/**
 * Description
 * 
 * Solution: -
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

		System.out.println("Bribe sums: "+Arrays.toString(bribe));
		System.out.println("Subordinates: "+subordinates);

		// Initialise three new arrays
		// m_bribe: The person gets bribed
		// m_notbribe: The person does not get bribed
		// m_notbribe_butchildren: The person does not get bribed, but at least one child is (which is a condition)

		int[] m_bribe = new int[numOfPeople];
		int[] m_notbribe = new int[numOfPeople];
		int[] m_notbribe_butchildren = new int[numOfPeople];

		// Base Cases, leafs
		for(int personIndex = 0; personIndex<numOfPeople; personIndex++) {
			if(subordinates.get(personIndex).size()==0) {
				m_bribe[personIndex] = bribe[personIndex];
				m_notbribe[personIndex] = 0;
				m_notbribe_butchildren[personIndex] = bribe[personIndex];
			}
		}

		System.out.println("m_bribe basecase: "+Arrays.toString(m_bribe));

		// Find the root of the tree and then the postorder, starting with leafs and then going up
		int root = findRoot(bosses, numOfPeople, leafs);
		System.out.println("Most sour excellence: "+root);
		Stack<Integer> postorder = dfs_postorder(subordinates, numOfPeople, root);
		System.out.println("Postorder stack: "+postorder);

		// Dynamic programming algorithm itself


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