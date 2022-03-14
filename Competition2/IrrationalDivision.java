import java.util.Arrays;

// https://open.kattis.com/problems/irrationaldivision

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