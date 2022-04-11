// https://open.kattis.com/problems/closestpair2
import java.awt.geom.Point2D;
import java.util.Arrays;
import java.util.Scanner;
import java.util.*;

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
			Arrays.sort(points, new Comparator<Point2D>() {
				public int compare(Point2D p1, Point2D p2) {
					return (int)Math.signum(p1.getX() - p2.getX());
				}
			});
			System.out.println(Arrays.toString(points));
			System.out.println("Minimal Points Distance: " + getMinDistance(points, 0, points.length));
		}
	
    }
	

	public static double getMinDistance(Point2D[] points, int a, int b){
		if(b-a<=3){
			if(b-a == 1){
				return -1.0;
			}
			double min = points[a].distance(points[a+1]);
			if(b-a>2){
				min = Math.min(min, points[a+1].distance(points[a+2]));
				min = Math.min(min, points[a+2].distance(points[a]));
			}
			return min;
		}
		int mid = (a+b)/2;
		double minL = getMinDistance(points, a, a+mid);
		double minR = getMinDistance(points, a+mid, b);
		double delta = Math.min(minL, minR);
		ArrayList<Point2D> slice = new ArrayList<Point2D>();
		double line = points[a+mid].getX();
		
		Point2D[] pointsByY = Arrays.copyOfRange(points, a, b);
		Arrays.sort(pointsByY, new Comparator<Point2D>() {
			public int compare(Point2D p1, Point2D p2) {
				return (int)Math.signum(p1.getY() - p2.getY());
			}
		});

		for (Point2D p : pointsByY) {
			if(Math.abs(p.getX()-line)<delta){
				slice.add(p);
			}
		}
		if(slice.size()<2){
			return delta;
		}
		double newMin = delta;
		for(int i = 0; i<slice.size();i++){
			for(int j = i+1; j<slice.size()&&j-i<16; j++){
				double distance = slice.get(i).distance(slice.get(j));
				if(distance<newMin){
					newMin = distance;
				}
			}
		}

		return newMin;
	}
}
