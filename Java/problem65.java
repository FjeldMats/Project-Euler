import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class problem65 {

	public static void main(String[] args) {
		
		ArrayList<Integer> continued = new ArrayList<Integer>();
		
		for(int i= 0;i<100;i++) {
			continued.add(2);
		}
		
		List<Integer> frac1 = Arrays.asList(1,2);
		List<Integer> frac2 = Arrays.asList(2,4);
		
		System.out.println(addFraction(frac1,frac2));
		System.out.println(numberToFrac(3));		
	}
	
	
	
	
	public static ArrayList<Integer> numberToFrac(int n){
		ArrayList<Integer> lst = new ArrayList<Integer>();
		
		lst.add(n);
		lst.add(1);
		return lst;
	}
	
	public static ArrayList<Integer> addFraction(List<Integer> n1, List<Integer> n2){
		

		ArrayList<Integer> finalFrac = new ArrayList<Integer>();
		ArrayList<Integer> frac1 = new ArrayList<Integer>();
		ArrayList<Integer> frac2 = new ArrayList<Integer>();
		
		
		frac1 = simplified(n1.get(0), n1.get(1));
		frac2 = simplified(n2.get(0), n2.get(1));
		
		System.out.println(frac1 + " " +  frac2);
		
		finalFrac.add(frac1.get(0) + frac2.get(0));
		finalFrac.add(frac1.get(1));
		finalFrac = simplified(finalFrac.get(0), finalFrac.get(1));
		
		return finalFrac;
	}
	
	public static ArrayList<Integer> simplified(int numerator, int denominator){
		int factor = 0;
		ArrayList<Integer> simple = new ArrayList<Integer>();
		for(int i= 1; i < denominator+1;i++) {
			if(numerator%i == 0 && denominator%i == 0) {
				factor = i;
			}
		}
		simple.add((int)(numerator/factor));
		simple.add((int) (denominator/factor));
		
		return simple;
	}
	
	public ArrayList<Integer> continuedFrac(int n, ArrayList<Integer> lst){
		return lst;
	}

}