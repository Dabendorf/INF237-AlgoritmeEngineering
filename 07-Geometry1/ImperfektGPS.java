// https://open.kattis.com/problems/imperfectgps
import java.awt.geom.Point2D;
import java.util.Arrays;

/**
 * There are given coordinates and timestamps when a walker was at these positions.
 * Also, there is a time intervall at which GPS measures the positions.
 * Calculate how much the GPS distance differs from the real walking distance
 * 
 * Solution: There are four arrays, one for given points, one for the given timestamps
 * The same exists for the GPS coordinates and time stamps.
 * The GPS timestamps get calculated by the given intervall, the points are calculated given that.
 * I loop through the GPS times and look if they have corresponding times in the original time array.
 * If this is the case, I copy the points. If not, I use binary search to find the timestamps at the left and the right.
 * From that, I calculate the point in between.
 * Then, given these two point arrays, I calculate both sums of distances and return the difference of them.
 */
public class ImperfektGPS {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		// Reading cases
        int numOfPositions = io.getInt();
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

		// Getting the maximum time
		int maxTime = times[numOfPositions-1];

		// Sum all the original distances
		double sumOriginalDistances = 0;
		for(int pointNum=0; pointNum < numOfPositions-1; pointNum++) {
			sumOriginalDistances += points[pointNum].distance(points[pointNum+1]);
		}

		// Calculate the timestamps of the GPS functionality
		int numOfGPStimes = (int)(Math.ceil(maxTime/intervallLength)+1);
		int[] gpsTimes = new int[numOfGPStimes];

		for(int gpsTimeNum=0; gpsTimeNum < numOfGPStimes; gpsTimeNum++) {
			int gpsTime = intervallLength*gpsTimeNum;
			gpsTime = Math.min(gpsTime, maxTime);
			gpsTimes[gpsTimeNum] = gpsTime;
		}

		// if the last point is missing, add it
		if(gpsTimes[gpsTimes.length-1] < times[times.length-1]) {
			int newGPStimes[] = new int[gpsTimes.length+1];
  
			for(int i=0; i<gpsTimes.length; i++) {
				newGPStimes[i] = gpsTimes[i];
			}
				
			newGPStimes[gpsTimes.length] = times[times.length-1];
			gpsTimes = newGPStimes;
			numOfGPStimes++;
		}

		// Calculate the GPS points
		Point2D[] gpsPoints = new Point2D[numOfGPStimes];

		for(int i=0; i<numOfGPStimes; i++) {
			int nextGPStime = gpsTimes[i];

			int posInTimes = Arrays.binarySearch(times, nextGPStime);

			if(posInTimes > -1) {
				gpsPoints[i] = points[posInTimes];
			} else {
				posInTimes = -posInTimes-1;
				gpsPoints[i] = findMiddlePoint(points[posInTimes-1], points[posInTimes+0], time_percentage(times[posInTimes-1], times[posInTimes+0], nextGPStime));
			}
			
		}

		// Sum the distance of GPS points
		double sumGPSDistances = 0;
		for(int pointNum=0; pointNum < numOfGPStimes-1; pointNum++) {
			sumGPSDistances += gpsPoints[pointNum].distance(gpsPoints[pointNum+1]);
		}

		// Output the difference
		double output = (1-sumGPSDistances/sumOriginalDistances)*100;

		if(Arrays.equals(times, gpsTimes)) {
			System.out.println(0.0);
		} else {
			System.out.println(output);
		}

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

	/**
	 * Finds a point on the line between two points depending on percental position
	 * (0=p, 1=q, 0.25=25% on the line between p and q)
	 * @param p Left point
	 * @param q Right point
	 * @param percentage Between 0 and 1
	 * @return Returns new Point2D
	 */
	private static Point2D findMiddlePoint(Point2D p, Point2D q, double percentage) {
		return new Point2D.Double(p.getX() + (q.getX()-p.getX()) * percentage, p.getY() + (q.getY()-p.getY()) * percentage);
	}

}