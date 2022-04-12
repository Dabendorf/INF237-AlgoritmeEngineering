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

			ReturnType r = getMinDistance(points, 0, points.length);
			System.out.println(r.a.getX()+" "+r.a.getY()+" "+r.b.getX()+" "+r.b.getY());
		}
	
    }
	

	public static ReturnType getMinDistance(Point2D[] points, int a, int b){
		if(b-a<=3){
			/*if(b-a == 1){
				return -1.0;
			}*/
			Point2D returnA = points[a];
			Point2D returnB = points[a+1];
			double min = points[a].distance(points[a+1]);
			if(b-a>2){
				//min = Math.min(min, points[a+1].distance(points[a+2]));
				double newDist = points[a+1].distance(points[a+2]);
				if(newDist < min) {
					returnA = points[a+1];
					returnB = points[a+2];
					min = newDist;
				}
				newDist = points[a+2].distance(points[a]);
				if(newDist < min) {
					returnA = points[a+2];
					returnB = points[a];
					min = newDist;
				}
				//min = Math.min(min, points[a+2].distance(points[a]));
			}
			return new ReturnType(min, returnA, returnB);
		}
		int mid = Math.abs(a-b)/2;
		//double minL = getMinDistance(points, a, a+mid);
		//double minR = getMinDistance(points, a+mid, b);
		ReturnType minLType = getMinDistance(points, a, a+mid);
		ReturnType minRType = getMinDistance(points, a+mid, b);
		double minL = minLType.minDist;
		double minR = minLType.minDist;
		double delta;
		Point2D returnA;
		Point2D returnB;
		if(minL<minR) {
			returnA = minLType.a;
			returnB = minLType.b;
			delta = minL;
		} else {
			returnA = minRType.a;
			returnB = minRType.b;
			delta = minR;
		}
		ArrayList<Point2D> slice = new ArrayList<Point2D>(16);
		double line = points[a+mid].getX();
		
		//Point2D[] pointsByY = Arrays.copyOfRange(points, a, b);
		Arrays.sort(points,a,b, new Comparator<Point2D>() {
			public int compare(Point2D p1, Point2D p2) {
				return (int)Math.signum(p1.getY() - p2.getY());
			}
		});

		for (int i = a; i<b; i++) {
			if(Math.abs(points[i].getX()-line)<delta){
				slice.add(points[i]);
			}
		}
		if(slice.size()<2){
			//return delta;
			return new ReturnType(delta, returnA, returnB);
		}
		double newMin = delta;
		//Point2D returnA;
		//Point2D returnB;
		for(int i = 0; i<slice.size();i++){
			for(int j = i+1; j<slice.size()&&j-i<8; j++){//Evil Pls Fix
				double distance = slice.get(i).distance(slice.get(j));
				if(distance<newMin){
					newMin = distance;
					returnA = slice.get(i);
					returnB = slice.get(j);
				}
			}
		}

		return new ReturnType(newMin, returnA, returnB);
	}
}
