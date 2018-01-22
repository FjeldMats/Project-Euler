public class euler46 {

	public static void main(String[] args) {
		
		for(int i=1; i<100;i++) {
			for(int j=1;j<100;j++){
				
				long comp = Composite(j,i);
				long Pnum = 2;
				while (Pnum<comp) {
					if(isPrime(Pnum)) {
						for(long square = 1; square<comp; square++) {
							//System.out.println(comp + " = " + Pnum + " + " + square+ " ^2 = " + Pnum + 2*square*square );
							long sum = Pnum + 2*square*square;
							if(comp == sum) {
								System.out.println(comp + " = " + Pnum + " + 2 * " + square+ "^2 = "+ sum );
							}
							else {
								break;
							}
						}
					}
					
					Pnum++;
				}
			}
		}
	}
	
	public static int Composite(int x, int y) {
		
		return 2*x -1 + 4*y*(x+y);
	}
	
	public static boolean isPrime(double n) {
		for(double i = 2; i < n; i++) {
			if(n%i == 0) {
				return false;
			}
		}
		return true;
	}

}
