// https://open.kattis.com/problems/citrusintern

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
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

		for(int i=0; i<numOfPeople; i++) {
			bribe[i] = io.getInt();
			int numOfSubordinates = io.getInt();
			
			subordinates.add(new TreeSet<Integer>());
			for(int j=0; j<numOfSubordinates; j++) {
				subordinates.get(i).add(io.getInt());
			}

		}

		System.out.println(Arrays.toString(bribe));
		System.out.println(subordinates);

		io.close();
	}

}