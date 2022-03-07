// https://open.kattis.com/problems/imperfectgps
import java.awt.geom.Point2D;
import java.util.Arrays;

/**
 * Problem description
 * 
 * Solution: 
 */
public class ImperfektGPS {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		// Reading cases
        /*int numOfPositions = io.getInt();
		int intervallLength = io.getInt();

		Point2D[] points = new Point2D[numOfPositions];
		int[] times = new int[numOfPositions];
		for(int posNum=0; posNum<numOfPositions; posNum++) {
			int x = io.getInt();
			int y = io.getInt();
			int t = io.getInt();

			points[posNum] = new Point2D.Double(x, y);
			times[posNum] = t;
		}

		int maxTime = times[numOfPositions-1];
		System.out.println("MaxTime: "+maxTime);
		System.out.println("Num of GPS times: "+(Math.ceil(maxTime/2.0)+1));
		

		System.out.println(Arrays.toString(points));
		System.out.println(Arrays.toString(times));

		double sumOriginalDistances = 0;
		for(int pointNum=0; pointNum < numOfPositions-1; pointNum++) {
			sumOriginalDistances += points[pointNum].distance(points[pointNum+1]);
		}

		System.out.println(sumOriginalDistances);

		for(int gpsTimeNum=0; gpsTimeNum < (int)(Math.ceil(maxTime/2.0)+1); gpsTimeNum++) {
			int gpsTime = intervallLength*gpsTimeNum;
			gpsTime = Math.min(gpsTime, maxTime);
		}*/

		int time0 = 3;
		int time1 = 9;
		Point2D p0 = new Point2D.Double(1, 1);
		Point2D p1 = new Point2D.Double(3, 5);
		int timeGPS = 9;
		System.out.println(findMiddlePoint(p0, p1, time_percentage(time0, time1, timeGPS)));

		// Working until here

		//  getLineFromPoints(Point2D p, Point2D q)

		/*System.out.println(time_percentage(1, 5, 1)); // 0
		System.out.println(time_percentage(1, 5, 5)); // 1

		System.out.println(time_percentage(1, 5, 3)); // 0.5
		System.out.println(time_percentage(1, 5, 2)); // 0.25
		System.out.println(time_percentage(1, 5, 0)); // oob
		System.out.println(time_percentage(1, 5, 6)); // oob
		System.out.println(time_percentage(5, 11, 7));

		System.out.println("==========");
		System.out.println(distBetweenPoints(new Point2D.Double(0, 0), new Point2D.Double(0, 0)));
		System.out.println(distBetweenPoints(new Point2D.Double(0, 0), new Point2D.Double(5, 0)));
		System.out.println(distBetweenPoints(new Point2D.Double(0, 0), new Point2D.Double(5, 5)));*/
		
		//System.out.println(getLineFromPoints(new Point2D.Double(0, 0), new Point2D.Double(5, 5)));
		io.close();
	}

	/**
	 * Calculates how much percentage of time a moment is in between two others
	 * (example: 2.0 is 0.25 between 1.0 and 5.0)
	 * @param begin Beginning time
	 * @param end Ending time
	 * @param between Moment in between
	 * @return Value between 0 and 1
	 */
	private static double time_percentage(int start, int end, int between) {
		if(between == start) {
			return 0.0;
		} else if(between == end) {
			return 1.0;
		} 

		double diff = end-start;

		double perc = (between-start)/diff;

		if(perc < 0 || perc > 1) {
			System.err.println("Percentage function out of bounds");
		}
		return perc;
	}

	/*private static double distBetweenPoints(Point2D p, Point2D q) {
		return p.distance(q);
	}*/

	private static String getLineFromPoints(Point2D p, Point2D q) {
		// find formula ax + by = c
		double diffY = q.getY() - p.getY();
		double diffX = p.getX() - q.getX();
		double c = diffY*(p.getX()) + diffX*(p.getY());

		if(diffX < 0) {
			return (diffY+"x"+" - "+diffX+"y = "+c);
		} else {
			return (diffY+"x"+" + "+diffX+"y = "+c);
		}
	}

	private static Point2D findMiddlePoint(Point2D p, Point2D q, double percentage) {
		return new Point2D.Double(p.getX() + (q.getX()-p.getX()) * percentage, p.getY() + (q.getY()-p.getY()) * percentage);
	}

}