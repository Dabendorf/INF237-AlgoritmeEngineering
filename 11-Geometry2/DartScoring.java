// https://uib.kattis.com/problems/dartscoring
import java.awt.geom.Point2D;
import java.util.Arrays;
import java.util.Scanner;

/**
 * Problem description
 * 
 * Solution: -
 */

 public class DartScoring {
    public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while(sc.hasNextLine()){
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
			
		}
	
    }

	
}