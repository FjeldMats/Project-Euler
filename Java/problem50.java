import java.util.ArrayList;
public class problem50 {

	public static void main(String[] args) {
		ArrayList<Integer> primes = new ArrayList<Integer>();
		int i = 2;
		int LIMIT = 1000000;
		while(i < LIMIT) {
			if(isPrime(i)){
				primes.add(i);
			}
			i++;
		}
		System.out.println("Primes listed: " + primes.size());
		
		int currentSum = 0;
		int currentNumber = 6;
		
		for(int i1 = 0; i1<primes.size(); i1++) {
			while(currentSum + currentNumber < LIMIT) {
				if(isPrime(currentNumber)) {
					currentSum  += currentNumber;
				}
				currentNumber++;
			}
		}
		
		System.out.println(currentSum);
		
	
		
		
	}
		
	
	public static boolean isPrime(int n) {
		if (n > 2 && n%2 == 0) {
	        return false;
	    }
	    int top = (int)Math.sqrt(n) + 3;
	    for(int i = 3; i < top; i+=2){
	        if(n % i == 0){
	            return false;
	        }
	    }
	    return true; 
	}
	
	public static int sumOfNumbersInList(int from, int to, ArrayList<Integer> list) {
		int sum = 0;
		
		
		for(int i = from; i<to; i++) {
			if(sum>1000000) {
				break;
			}
			sum += list.get(i);
		}
		return sum;
	}
}
