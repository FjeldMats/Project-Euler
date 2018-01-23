import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class problem33 {

	public static void main(String[] args) {
		
		ArrayList<ArrayList<Integer>> fraction = new ArrayList<ArrayList<Integer>>();
		for(int i = 11;i<100;i++) {
			for(int j=i+1;j<100;j++) {
				//System.out.println(i + " / " + j);
				ArrayList<Integer> nums = new ArrayList<Integer>();
				nums.add(i);
				nums.add(j);
				fraction.add(nums);
			}
		}
		int count = 0;
		ArrayList<Integer> product = null;
		int productOfNumerators = 1;
		int productOfDenominators = 1;
		for( int ind = 0; ind<fraction.size();ind++) {
			int numerator = curiousFrac(fraction.get(ind)).get(0);
			int denominator = curiousFrac(fraction.get(ind)).get(1);
			if(denominator != 0){
				
				productOfNumerators *= numerator;
				productOfDenominators *= denominator;
				product = simplified(productOfNumerators, productOfDenominators);
				count++;
			}
		}
		System.out.println(count + " fractions, product of the denominators: "+product.get(1));
		
	}
	
	public static ArrayList<Integer> curiousFrac(ArrayList<Integer> lst) {
		
		String firstNumStr = lst.get(0).toString();
		String secNumStr =lst.get(1).toString();
		
		List<String> firstNumList = new ArrayList<>(Arrays.asList(firstNumStr.split("")));
		List<String> secNumList = new ArrayList<>(Arrays.asList(secNumStr.split("")));
		
		ArrayList<Integer> curiousFrac = new ArrayList<Integer>();
		ArrayList<Integer> none = new ArrayList<Integer>();
		none.add(0);
		none.add(0);
		curiousFrac = findCommonNum(firstNumList,secNumList);
		if(curiousFrac == null) {
			return none;
		}
		else{
			
			if(curiousFrac.get(1) != 0) {
				ArrayList<Integer> frac1 = simplified(curiousFrac.get(0), curiousFrac.get(1));
				ArrayList<Integer> frac2 = simplified(lst.get(0), lst.get(1));
				if(compareList(frac1,frac2)){
					return frac1;
				}
			}
			
			return none;
		}
		
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
	
	public static ArrayList<Integer> findCommonNum(List<String> n1, List<String> n2){
		ArrayList<Integer> finalFraction = new ArrayList<Integer>();
		
		if(Integer.parseInt(n1.get(0)) == Integer.parseInt(n2.get(0)) && Integer.parseInt(n1.get(0)) != 0) {
			n1.remove(0);
			n2.remove(0);
		}
		else if(Integer.parseInt(n1.get(0)) == Integer.parseInt(n2.get(1))&& Integer.parseInt(n1.get(0)) != 0) {
			n1.remove(0);
			n2.remove(1);
		}
		else if(Integer.parseInt(n1.get(1)) == Integer.parseInt(n2.get(0))&& Integer.parseInt(n1.get(1)) != 0) {
			n1.remove(1);
			n2.remove(0);
		}
		else if(Integer.parseInt(n1.get(1)) == Integer.parseInt(n2.get(1))&& Integer.parseInt(n1.get(1)) != 0) {
			n1.remove(1);
			n2.remove(1);
		}
		else {
			return null;
		}
		//System.out.println(n1 + " - " + n2);
		
		finalFraction.add(Integer.parseInt(n1.get(0)));
		finalFraction.add(Integer.parseInt(n2.get(0)));
		return finalFraction;
	}
	
	public static boolean compareList(ArrayList<Integer> lst1, ArrayList<Integer> lst2 ) {
		return (lst1.get(0) == lst2.get(0) && lst1.get(1) == lst2.get(1));
	}
}
