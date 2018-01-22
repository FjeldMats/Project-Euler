import java.util.ArrayList;

public class problem47 {

	public static void main(String[] args) {
	
		int i = 2;
		int previ = 1;
		int inarow = 0; 
		
		while(inarow < 3) {
			if(countPrimeFactors(findFactors(i)) == 4) {
				System.out.println(i+ " " + findFactors(i));
				if(previ + 1 == i) {
					inarow++;
				}else {
					inarow = 0;
				}
				previ = i;
			}
			
			i++;
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
	
	public static ArrayList<Integer> findFactors(long n){
		
		ArrayList<Integer> factors = new ArrayList<Integer>();
		for(int i=2; i< n; i++ ) {
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
