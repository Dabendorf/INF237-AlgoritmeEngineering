import java.awt.geom.Point2D;
import java.util.Comparator;

class PointCmp implements Comparator<Point2D.Double> {
    public int compare(Point2D.Double a, Point2D.Double b) {
        return (a.x < b.x) ? -1 : (a.x > b.x) ? 1 : 0;
    }
}
