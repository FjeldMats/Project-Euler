import java.util.ArrayList;

public class euler47 {

	public static void main(String[] args) {
		
		int upperLim = 646;
		int i = 2;
		int previ = 0;
		int inarow = 0;
		
		while(i<=upperLim) {
			if(countPrimeFactors(findFactors(i)) >= 4) {
				if(previ == i - 1) {
					inarow++;
				}
				System.out.println(i+ " " + findFactors(i));
			}
			previ = i;
			i++;
		}
	}
	
	public static boolean isPrime(double n) {
		for(double i = 2; i < (int) Math.sqrt(n) + 5; i++) {
			if(n%i == 0) {
				return false;
			}
		}
		return true;
	}
	
	public static ArrayList<Integer> findFactors(long n){
		
		ArrayList<Integer> factors = new ArrayList<Integer>();
		for(int i=2; i< (int) Math.sqrt(n) + 5; i++ ) {
			if(n%i == 0) {
				factors.add(i);
			}
		}
		return factors;
	}
	
	public static int countPrimeFactors(ArrayList<Integer> factors) {
		int count = 0;
		
		for(int number: factors) {
			if(isPrime(number)) {
				count++;
			}
		}
		return count;
	}
	
}
