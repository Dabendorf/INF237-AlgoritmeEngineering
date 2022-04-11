// https://open.kattis.com/problems/closestpair2
import java.awt.geom.Point2D;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Problem description
 * 
 * Solution: -
 */
public class ClosestPair {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		boolean scanNextStuff = true;
		while(scanNextStuff) {
			String numPointsStr = sc.nextLine();
			if(numPointsStr.equals("0")) {
				scanNextStuff = false;
				break;
			}

			int numPoints = Integer.parseInt(numPointsStr);

			Point2D[] points = new Point2D[numPoints];
			for(int i=0; i<numPoints; i++) {
				String sor=sc.nextLine();
				String[] splitted = sor.split(" ");
				points[i] = new Point2D.Double(Double.parseDouble(splitted[0]), Double.parseDouble(splitted[1]));
			}
			System.out.println(Arrays.toString(points));
		}
		/*while(sc.hasNextLine()){
			// each test case
			String sor=sc.nextLine();
			String[] splitted = sor.split(" ");
			System.out.println(Arrays.toString(splitted));
			
			int lengthList =  splitted.length/2;
			Point2D[] points = new Point2D[lengthList];
			for(int i=0; i<(int) splitted.length/2; i++) {
				points[i] = new Point2D.Double(Double.parseDouble(splitted[2*i]), Double.parseDouble(splitted[2*i+1]));
			}

			Arrays.sort(points, (o1, o2) -> (int)Math.signum(o1.getX()-o2.getX()));
			System.out.println("Sorted Array by x:");
			double min = getMinDistance(points, 0, points.length);
			System.out.println("Der minimale Abstand beträgt: "+min);
			
		}*/
	
    }
	

	public static double getMinDistance(Point2D[] points, int a, int b){
		if(b-a<=3){
			if(b-a == 1){
				return 0.0;
			}
			double min = points[a].distance(points[a+1]);
			if(b-a>2){
				min = Math.min(min, points[a+1].distance(points[a+2]));
				min = Math.min(min, points[a+2].distance(points[a]));
			}
			return min;
		}

		return 0.0;
	}
}
