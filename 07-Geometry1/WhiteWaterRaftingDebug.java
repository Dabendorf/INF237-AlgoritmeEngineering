// https://open.kattis.com/problems/rafting
import java.util.Arrays;
import java.awt.geom.Point2D;

/**
 * There are an inner and an outer polygon, which do not touch each other.
 * Moreover, there is a circular raft which rafts through the inner path between those polygons.
 * Find the biggest possible radius of the raft s.t. this is possible
 * 
 * Solution: 
 */
public class WhiteWaterRaftingDebug {
    public static void main(String[] args) {

		//Point2D p3 = new Point2D.Double(0, 0);
		//System.out.println(p3.distance(1, 1));
        
		//int[] lineA = {-1, -1};
		//int[] lineB = {-4, 2};
		//int[] point = {0, 0};
		//int[] lineA = {0, 0};
		//int[] lineB = {5, 0};
		//int[] point = {2, 1};
		Point2D lineA = new Point2D.Double(0, 0);
		Point2D lineB = new Point2D.Double(5, 0);
		Point2D point = new Point2D.Double(2, 1);

		System.out.println("Line: "+lineA);
		System.out.println("Point: "+lineB);
		System.out.println("Dist: "+distance(lineA, lineB, point));
		// Calculate interception value on line segment
			
    }

	//public static double distance(int[] point_line0, int[] point_line1, int[] point_sep) {
	public static double distance(Point2D p1, Point2D p2, Point2D p3) {
		// First calculate interception value
		double delta_x_point = p3.getX() - p1.getX();
		double delta_y_point = p3.getY() - p1.getY();
		double delta_x_line = p2.getX() - p1.getX();
		double delta_y_line = p2.getY() - p1.getY();

		//int norm = delta_x_line * delta_x_line + delta_y_line * delta_y_line;
		System.out.println("Delta x Line: "+delta_x_line);
		System.out.println("Delta y Line: "+delta_y_line);
		System.out.println("Delta x Point: "+delta_x_point);
		System.out.println("Delta y Point: "+delta_y_point);

		//double intercept = (delta_x_point*delta_x_line + delta_y_point*delta_y_line) / norm;
		//System.out.println("Intercept value: "+intercept);

		//final double xDelta = p2.getX() - p1.getX();
		//final double yDelta = p2.getY() - p1.getY();

		double intercept = ((p3.getX() - p1.getX()) * delta_x_line + (p3.getY() - p1.getY()) * delta_y_line) / (delta_x_line * delta_x_line + delta_y_line * delta_y_line);
		
		//System.out.println("Intercept old "+intercept);
		double intercept_point_x;
		double intercept_point_y;

		if(intercept>=1) {
			intercept = 1;
			intercept_point_x = p2.getX();
			intercept_point_y = p2.getY();
			System.out.println("Set intercept to point 1");
		} else if(intercept<=0) {
			intercept = 0;
			intercept_point_x = p1.getX();
			intercept_point_y = p1.getY();
			System.out.println("Set intercept to point 0");
		} else {
			intercept_point_x = p1.getX() + intercept * (delta_x_line);
			intercept_point_y = p1.getY()+ intercept * (delta_y_line);
		}
		System.out.println("Intercept point: ("+intercept_point_x+","+intercept_point_y+")");

		

		// calculate final distance

		Point2D insect = new Point2D.Double(intercept_point_x, intercept_point_y);
		return insect.distance(p3.getX(), p3.getY());
		//return Math.sqrt(Math.pow(intercept_point_x-point_sep[0], 2)+Math.pow(intercept_point_y-point_sep[1], 2));
	}
}