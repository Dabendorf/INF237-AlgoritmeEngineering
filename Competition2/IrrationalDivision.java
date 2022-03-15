// https://open.kattis.com/problems/irrationaldivision

/**
 * There is a chess board with size pxq where the upper left one is black.
 * One player sits at p-side and one at q-side.
 * One can break apart as many rows/columns as one wants from where one sits.
 * Every black piece gives one point, every white piece minus one.
 * The player alternate their turns until the board is empty.
 * Output the maximum point distance between both players
 * 
 * Solution: This can be solved with math. If both numbers (p and q) are odd, the solution is 1.
 * If p is even, the output is zero. If p is odd, one checks if q is bigger than p.
 * If so, the output is 2, otherwise 0.
 */
public class IrrationalDivision {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

		int p = io.getInt();
		int q = io.getInt();

		boolean pEven = p%2 == 0;
		boolean qEven = q%2 == 0;

		if(!pEven) {
			if(!qEven) {
				System.out.println(1);
			} else if (q > p) {
				System.out.println(2);
			} else {
				System.out.println(0);
			}
		} else {
			System.out.println(0);
		}

		io.close();
	}
}