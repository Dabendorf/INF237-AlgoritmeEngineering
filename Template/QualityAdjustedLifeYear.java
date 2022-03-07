public class QualityAdjustedLifeYear {
    public static void main(String[] args) {
        Kattio io = new Kattio(System.in, System.out);

        io.getInt();

		double sum = 0;
        while(io.hasMoreTokens()) {
			double a = io.getDouble();
			double b = io.getDouble();
			sum += (a*b);
		}

		io.println(sum);

        io.close();
    }
}
