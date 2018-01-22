
public class euler3 {

	public static void main(String[] args) {
		
		double number = 600851475143L;

		for(long i = 2; i<number-1; i++) {
			if( isPrime(i) && number%i == 0) {
				System.out.println(i);
			}
		}
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
