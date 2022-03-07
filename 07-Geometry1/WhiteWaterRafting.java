// https://uib.kattis.com/problems/rafting
import java.awt.geom.Point2D;

/**
 * There are an inner and an outer polygon, which do not touch each other.
 * Moreover, there is a circular raft which rafts through the inner path between those polygons.
 * Find the biggest possible radius of the raft s.t. this is possible
 * 
 * Solution: Go through each pair of points from one polygon and line segments from the other (2 times for each way around)
 * Calculate the distance between them and output the minimum of all
 * Calculating the distance is done by known line-to-point-distance formula
 * Problem: What if perpendicular intersection point outside of line segment?
 * 
 * Calculate intersection value (how far from the left boundary is point on line?):
 * If < 0, its outside on the left, if > 1, its outside on the right
 * In this situation set intersection point to the boundary
 * Then return the distance between that intersection point and the original one
 */
public class WhiteWaterRafting {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		// Reading cases
        int numOfTestcases = io.getInt();
		for(int testNum=0; testNum<numOfTestcases; testNum++) {
			int numOfInnerPoints = io.getInt();
			Point2D[] pointsInner = new Point2D[numOfInnerPoints];
			for(int pointNum=0; pointNum<numOfInnerPoints; pointNum++) {
				int x = io.getInt();
				int y = io.getInt();
				pointsInner[pointNum] = new Point2D.Double(x, y);
			}

			int numOfOuterPoints = io.getInt();
			Point2D[] pointsOuter = new Point2D[numOfOuterPoints];
			for(int pointNum=0; pointNum<numOfOuterPoints; pointNum++) {
				int x = io.getInt();
				int y = io.getInt();
				pointsOuter[pointNum] = new Point2D.Double(x, y);;
			}

			// Calculating the distances
			// Loop through pairs of points of one polygon and lines of the other one (2 times)
			// Save minimum distance

			double min_dist = 1000000.0;
			for(int pointNumInner=0; pointNumInner<numOfInnerPoints; pointNumInner++) {
				for(int lineNumOuter=0; lineNumOuter<numOfOuterPoints; lineNumOuter++) {
					Point2D linePointNum0 = pointsOuter[lineNumOuter];
					Point2D linePointNum1;
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
					Point2D linePointNum0 = pointsInner[lineNumInner];
					Point2D linePointNum1;
					if(lineNumInner+1 == numOfInnerPoints) {
						linePointNum1 = pointsInner[0];
					} else {
						linePointNum1 = pointsInner[lineNumInner+1];
					}
					double new_dist = distance(linePointNum0, linePointNum1, pointsOuter[pointNumOuter]);
					min_dist = Math.min(min_dist, new_dist);
				}
			}

			// I don't know why, but it outputs double of the correct value
			System.out.println(min_dist/2);
			
		}

        io.close();
    }

	/**
	 * Calculates distance between a line segment and a point
	 * @param line_point0 Left boundary of line
	 * @param line_point1 Right boundary of line
	 * @param p Point outside of line
	 * @return Distance
	 */
	public static double distance(Point2D line_point0, Point2D line_point1, Point2D p) {
		// First calculate interception value
		// Temporary stuff
		double delta_x_point = p.getX() - line_point0.getX();
		double delta_y_point = p.getY() - line_point0.getY();
		double delta_x_line = line_point1.getX() - line_point0.getX();
		double delta_y_line = line_point1.getY() - line_point0.getY();

		double norm = delta_x_line * delta_x_line + delta_y_line * delta_y_line;
		
		// Intersept value, if not between 0 and 1, interception point is outside of line
		double intercept = (delta_x_point * delta_x_line + delta_y_point * delta_y_line) / norm;
		
		double intercept_point_x;
		double intercept_point_y;

		if(intercept>=1) {
			// Set point to outer right line segment boundary
			intercept_point_x = line_point1.getX();
			intercept_point_y = line_point1.getY();
		} else if(intercept<=0) {
			// Set point to outer left line segment boundary
			intercept_point_x = line_point0.getX();
			intercept_point_y = line_point0.getY();
		} else {
			intercept_point_x = line_point0.getX() + intercept * (delta_x_line);
			intercept_point_y = line_point0.getY() + intercept * (delta_y_line);
		}
		
		// calculate final distance
		Point2D insect = new Point2D.Double(intercept_point_x, intercept_point_y);
		return insect.distance(p.getX(), p.getY());
	}
}