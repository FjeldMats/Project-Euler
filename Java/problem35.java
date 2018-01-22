import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class problem35 {

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
		System.out.println("list of: " + primes.size()+ " primes");
		int count = 0;
		for(int j=0;j<primes.size();j++) {
			if(isCircular(primes.get(j))){
				//System.out.println(primes.get(j));
				count++;
			}
		}
		
		System.out.println(count +" Circular primes below a million");
	}
	
	public static boolean isPrime(int n) {
		if (n > 2 && n%2 == 0) {
	        return false;
	    }
	    int top = (int)Math.sqrt(n) + 2;
	    for(int i = 3; i < top; i+=2){
	        if(n % i == 0){
	            return false;
	        }
	    }
	    return true; 
	}
	
	public static boolean isCircular(int n) {
		//ArrayList<String> numbers = new ArrayList<String>();
		String number = Integer.toString(n);
		String[] nums = number.split("");
		String newNum = "";
		List<String> listOfNums = new ArrayList<String>(Arrays.asList(nums));
		for(int i=0;i<listOfNums.size();i++) {
			newNum = "";
			listOfNums = rotate(listOfNums);
			for (String elm:listOfNums){
				newNum = newNum + elm;
			}
			if(!isPrime(Integer.parseInt(newNum))) {
				return false;
			}
		}
		return true;
	}
	
	public static List<String> rotate(List<String> lst){
		String last = lst.get(lst.size()-1);
		lst.remove(lst.size()-1);
		lst.add(0, last);
		return lst;
	}

}
