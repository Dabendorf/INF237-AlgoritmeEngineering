// https://uib.kattis.com/problems/rubiksrevenge

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class RubiksRevanche {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		int[] pos_temp = new int[16];
		int[] orig_pos = {0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3};

		for(int i=0; i<4; i++) {
			String new_line = io.getWord();
			for(int j=0; j<4; j++) {
				char c = new_line.charAt(j);
				if(c=='R') {
					pos_temp[4*i+j] = 0;
				} else if(c=='G') {
					pos_temp[4*i+j] = 1;
				} else if(c=='B') {
					pos_temp[4*i+j] = 2;
				} else {
					pos_temp[4*i+j] = 3;
				}
				//{"R":0, "G":1, "B":2, "Y":3}
			}
		}
		//System.out.println(Arrays.toString(pos_temp));

		int orig_positions = listToBin(orig_pos);
		int goal_positions = listToBin(pos_temp);

		System.out.println(bidirectional_search(orig_positions, goal_positions));
		
	}

	static int bidirectional_search(int start, int goal) {
		// Every state is represented by an integer (binary number with 32 digits where pairs of 2 are the colour at one position)
		// This neighbouring function works 100% correct, I checked this

		// Sets of visited states from start and end
		Set<Integer> visited_start = new HashSet<Integer>();
		Set<Integer> visited_end = new HashSet<Integer>();

		// Parents of visited states (where did we visit them from)
		//parent_start = defaultdict(lambda: -1)
		//parent_end = defaultdict(lambda: -1)
		Map<Integer, Integer> parent_start = new HashMap<Integer, Integer>();
		Map<Integer, Integer> parent_end = new HashMap<Integer, Integer>();

		// Queues for the bidirectional search
		ArrayList<Integer> queue_start = new ArrayList<>();
		queue_start.add(start);
		ArrayList<Integer> queue_goal = new ArrayList<>();
		queue_goal.add(goal);

		visited_start.add(start);
		visited_end.add(goal);

		int pointer_start = 0;
		int pointer_goal = 0;
		parent_start.put(start, -1);
		parent_end.put(goal, -1);

		// The middle point where both BFSs will meet each other
		int meeting_point = -1; // later used together with parent to find the depth
		
		boolean found = false;
		// This still seems terribly slow
		// This must change to pointer < length, but since there always is a solution, this should be a problem
		//while queue_start and queue_goal and meeting_point is None:
		while(meeting_point == -1) {
			// Forward direction
			int s = queue_start.get(pointer_start);
			pointer_start += 1;

			for(int u: neighbours(s)) {
				if(!visited_start.contains(u)) {
					queue_start.add(u);
					visited_start.add(u);
					parent_start.put(u, s);
				}
			}

			if(s == goal || queue_goal.contains(s)) {
				meeting_point = s;
				found = true;
				break;
			}

			// Backwards direction
			int t = queue_goal.get(pointer_goal);
			pointer_goal += 1;

			for(int v: neighbours(t)) {
				if(!visited_end.contains(v)) {
					queue_goal.add(v);
					visited_end.add(v);
					parent_end.put(v, t);
				}
			}

			if(t == start || queue_start.contains(t)) {
				meeting_point = t;
				found = true;
				break;
			}
		
		}
		//debug(meeting_point)
		// Calculate the length of the path (I guess this is wrong?)
		int path_start = 0;
		int node1 = meeting_point;
		//System.out.println(visited_start.size());
		//System.out.println(visited_end.size());
		while(node1 != -1) {
			path_start += 1;

			if(parent_start.containsKey(node1)) {
				node1 = parent_start.get(node1);
			} else {
				break;
			}
			
		}

		int path_end = 0;
		int node2 = parent_end.get(meeting_point);
		while(node2 != -1) {
			path_end += 1;
			if(parent_end.containsKey(node2)) {
				node2 = parent_end.get(node2);
			} else {
				break;
			}
		}

		return path_start+path_end-1;
	}

	static int listToBin(int[] l) {
		int out = l[0];
		for(int i=1; i<16; i++) {
			out = out << 2;
			out += l[i];
		}
		return out;
	}

	static int swap_positions(int pattern, int ind0, int ind1, int ind2, int ind3, boolean left) {
		int mask0 = 3 << ind0*2;
		int mask1 = 3 << ind1*2;
		int mask2 = 3 << ind2*2;
		int mask3 = 3 << ind3*2;

		int val0 = pattern & mask0;
		int val1 = pattern & mask1;
		int val2 = pattern & mask2;
		int val3 = pattern & mask3;

		pattern = pattern & ~mask0;
		pattern = pattern & ~mask1;
		pattern = pattern & ~mask2;
		pattern = pattern & ~mask3;

		val0 >>= ind0*2;
		val1 >>= ind1*2;
		val2 >>= ind2*2;
		val3 >>= ind3*2;

		if(left) {
			pattern |= val0 << ind1*2;
			pattern |= val1 << ind2*2;
			pattern |= val2 << ind3*2;
			pattern |= val3 << ind0*2;
		} else {
			pattern |= val0 << ind3*2;
			pattern |= val1 << ind0*2;
			pattern |= val2 << ind1*2;
			pattern |= val3 << ind2*2;

		}
		return pattern;
	}

	static int[] neighbours(int pos) {
		int[] stuff = new int[16];
		stuff[0] = swap_positions(pos, 0,1,2,3, false);
		stuff[1] = swap_positions(pos, 4,5,6,7, false);
		stuff[2] = swap_positions(pos, 8,9,10,11, false);
		stuff[3] = swap_positions(pos, 12,13,14,15, false);
		stuff[4] = swap_positions(pos, 0,1,2,3, true);
		stuff[5] = swap_positions(pos, 4,5,6,7, true);
		stuff[6] = swap_positions(pos, 8,9,10,11, true);
		stuff[7] = swap_positions(pos, 12,13,14,15, true);
		stuff[8] = swap_positions(pos, 0,4,8,12, false);
		stuff[9] = swap_positions(pos, 1,5,9,13, false);
		stuff[10] = swap_positions(pos, 2,6,10,14, false);
		stuff[11] = swap_positions(pos, 3,7,11,15, false);
		stuff[12] = swap_positions(pos, 0,4,8,12, true);
		stuff[13] = swap_positions(pos, 1,5,9,13, true);
		stuff[14] = swap_positions(pos, 2,6,10,14, true);
		stuff[15] = swap_positions(pos, 3,7,11,15, true);
		return stuff;
	}

}