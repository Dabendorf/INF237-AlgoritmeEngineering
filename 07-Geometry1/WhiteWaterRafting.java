// https://open.kattis.com/problems/rafting
import java.util.Arrays;

/**
 * There are an inner and an outer polygon, which do not touch each other.
 * Moreover, there is a circular raft which rafts through the inner path between those polygons.
 * Find the biggest possible radius of the raft s.t. this is possible
 * 
 * Solution: 
 */
public class WhiteWaterRafting {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		// Reading cases
        int numOfTestcases = io.getInt();
		for(int testNum=0; testNum<numOfTestcases; testNum++) {
			int numOfInnerPoints = io.getInt();
			int[][] pointsInner = new int[numOfInnerPoints][];
			for(int pointNum=0; pointNum<numOfInnerPoints; pointNum++) {
				int x = io.getInt();
				int y = io.getInt();
				pointsInner[pointNum] = new int[]{x, y};
			}

			int numOfOuterPoints = io.getInt();
			int[][] pointsOuter = new int[numOfOuterPoints][];
			for(int pointNum=0; pointNum<numOfOuterPoints; pointNum++) {
				int x = io.getInt();
				int y = io.getInt();
				pointsOuter[pointNum] = new int[]{x, y};
			}

			// Calculating the distances

			System.out.println(Arrays.deepToString(pointsInner));
			System.out.println(Arrays.deepToString(pointsOuter));

			// Potential correct code
			
			double min_dist = 1000000.0;
			for(int pointNumInner=0; pointNumInner<numOfInnerPoints; pointNumInner++) {
				for(int lineNumOuter=0; lineNumOuter<numOfOuterPoints; lineNumOuter++) {
					int[] linePointNum0 = pointsOuter[lineNumOuter];
					int[] linePointNum1;
					if(lineNumOuter+1 == numOfOuterPoints) {
						linePointNum1 = pointsOuter[0];
					} else {
						linePointNum1 = pointsOuter[lineNumOuter+1];
					}
					double new_dist = distance(linePointNum0, linePointNum1, pointsInner[pointNumInner]);
					min_dist = Math.min(min_dist, new_dist);
				}
			}

			for(int pointNumOuter=0; pointNumOuter<numOfOuterPoints; pointNumOuter++) {
				for(int lineNumInner=0; lineNumInner<numOfInnerPoints; lineNumInner++) {
					int[] linePointNum0 = pointsInner[lineNumInner];
					int[] linePointNum1;
					if(lineNumInner+1 == numOfInnerPoints) {
						linePointNum1 = pointsInner[0];
					} else {
						linePointNum1 = pointsInner[lineNumInner+1];
					}
					double new_dist = distance(linePointNum0, linePointNum1, pointsOuter[pointNumOuter]);
					min_dist = Math.min(min_dist, new_dist);
				}
			}

			System.out.println(min_dist);

			//System.out.println(distance(pointsOuter[0], pointsOuter[1], pointsInner[0]));
			
			/*int[] lineA = {-1, -1};
			int[] lineB = {-4, 2};
			int[] point = {0, 0};
			System.out.println("Dist: "+distance(lineA, lineB, point));*/
			// Calculate interception value on line segment
			
		}

        io.close();
    }

	public static double distance(int[] point_line0, int[] point_line1, int[] point_sep) {
		/*System.out.println("======");
		System.out.println(Arrays.toString(point_line0));
		System.out.println(Arrays.toString(point_line1));
		System.out.println(Arrays.toString(point_sep));*/

		// First calculate interception value
		int delta_x_point = point_sep[0] - point_line0[0];
		int delta_y_point = point_sep[1] - point_line0[1];
		int delta_x_line = point_line1[0] - point_line0[0];
		int delta_y_line = point_line1[1] - point_line0[1];

		int norm = delta_x_line * delta_x_line + delta_y_line * delta_y_line;

		double intercept = (delta_x_point*delta_x_line + delta_y_point*delta_y_line) / norm;

		// find orthogonal point on line
		
		//System.out.println("Intercept old "+intercept);
		if(intercept>1) {
			intercept = 1;
		} else if(intercept<0) {
			intercept = 0;
		}

		//System.out.println("Intercept new: "+intercept);
		double intercept_point_x = point_line0[0] + intercept * (delta_x_line);
		double intercept_point_y = point_line0[1] + intercept * (delta_y_line);
		//System.out.println(intercept_point_x);
		//System.out.println(intercept_point_y);
		

		// calculate final distance

		return Math.sqrt(Math.pow(intercept_point_x-point_sep[0], 2)+Math.pow(intercept_point_y-point_sep[1], 2));
	}
}