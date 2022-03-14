// https://open.kattis.com/contests/miojc3/problems/dirtydriving
import java.awt.geom.Point2D;
import java.util.Arrays;
import java.util.Collections;

public class DirtyDriving {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		// Reading cases
        int numOfCars = io.getInt();
		int deceleration = io.getInt();

		int[] carsAhead = new int[numOfCars];

		for(int i=0; i<numOfCars; i++) {
			carsAhead[i] = io.getInt();
		}
		Arrays.sort(carsAhead);

		//System.out.println(Arrays.toString(carsAhead));

		long dist = 0;
		for(int i=0; i<numOfCars; i++) {
			long dist1 = deceleration * (i+1);
			long dist2 = carsAhead[i];
			dist = Math.max(dist, dist1-dist2);
		}

		System.out.println(dist+carsAhead[0]);

		io.close();
	}

}