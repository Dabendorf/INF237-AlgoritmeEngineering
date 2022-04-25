// https://uib.kattis.com/problems/dartscoring
import java.awt.geom.Point2D;
import java.util.ArrayList;
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
			System.out.println("=============");
			String sor=sc.nextLine();
			String[] splitted = sor.split(" ");
			//System.out.println(Arrays.toString(splitted));
			
			int lengthList =  splitted.length/2;
			Point2D[] points = new Point2D[lengthList];
			for(int i=0; i<(int) splitted.length/2; i++) {
				points[i] = new Point2D.Double(Double.parseDouble(splitted[2*i]), Double.parseDouble(splitted[2*i+1]));
			}

			Arrays.sort(points, (o1, o2) -> (int)Math.signum(o1.getY()-o2.getY()));

			ArrayList<Point2D> S = new ArrayList<Point2D>();
			ArrayList<Point2D> hull = new ArrayList<Point2D>();
			ArrayList<Point2D> hull2 = new ArrayList<Point2D>();

			for(Point2D p: points) {
				while(S.size() >= 2 && leftturn(S.get(S.size()-2), S.get(S.size()-1), p)) {
					S.remove(S.size() - 1);
				}
				S.add(p);
			}
			
			for(Point2D el:S) {
				hull.add(el);
			}
			System.out.println("Hull1: "+hull+"\n");

			S = new ArrayList<Point2D>();
			//Collections.reverse(points);
			System.out.println("points: "+Arrays.toString(points));
			points = reverse(points, points.length);
			for(Point2D p: points) {
				while(S.size() >= 2 && leftturn(S.get(S.size()-2), S.get(S.size()-1), p)) {
					S.remove(S.size() - 1);
				}
				S.add(p);
			}

			for(int i=1; i<S.size()-1;i++) {
				hull2.add(S.get(i));
			}
			System.out.println("Hull2: "+hull2+"\n");

			//System.out.println(hull);

			double stringLength = 0;

			for(int i=0; i<hull.size()-1;i++) {
				stringLength += hull.get(i).distance(hull.get(i+1));
			}
			stringLength += hull.get(0).distance(hull.get(hull.size()-1));

			double finalScore = 100*points.length/(1+stringLength);

			System.out.println(finalScore);
		}
		
	
    }

	static int getOrientation(Point2D p1, Point2D p2, Point2D p3) {
		double area = (p2.getY()-p1.getY())*(p3.getX()-p2.getX())-(p2.getX()-p1.getX())*(p3.getY()-p2.getY());
		if(area > 0) {
			return 1;
		}

		if(area < 0) {
			return -1;
		} 
		return 0;
	}

	public static boolean leftturn(Point2D p1, Point2D p2, Point2D p3){
		double area = (p2.getY()-p1.getY())*(p3.getX()-p2.getX())-(p2.getX()-p1.getX())*(p3.getY()-p2.getY());
		return area<0; 
	}
	
	public static Point2D[] reverse(Point2D[] a, int n) {
        Point2D[] b = new Point2D[n];
        int j = n;
        for (int i = 0; i < n; i++) {
            b[j - 1] = a[i];
            j = j - 1;
        }
		return b;
    }
}