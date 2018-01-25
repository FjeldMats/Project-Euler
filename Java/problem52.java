import java.util.ArrayList;
import java.util.Collections;

public class problem52 {

	public static void main(String[] args) {
		
		int number = 1234;
		
		while(!(containsSameDigits(integerToArray(number),integerToArray(number*2)) && 
				containsSameDigits(integerToArray(number*3),integerToArray(number*4)) &&
				containsSameDigits(integerToArray(number*5), integerToArray(number*6)))) {
			number++;
		}
				
		System.out.println(number);

	}

	public static boolean containsSameDigits(ArrayList<Integer> lst1, ArrayList<Integer> lst2) {
		int digits = 0;
		if(lst2.size() != lst1.size()) {
			return false;
		}
		for(int i=0;i<lst1.size();i++) {
			for(int j=0;j<lst2.size();j++) {
				if(lst1.get(i) == lst2.get(j)) {
					digits++;
					lst2.remove(j);
				}
			}
		}
		
		if(digits == lst1.size()) {
			return true;
		}
		
		return false;
	}
	
	public static ArrayList<Integer> integerToArray(int number){
		ArrayList<Integer> lst = new ArrayList<Integer>();
		while (number>10) {
			int lastDigit = number%10;
			lst.add(lastDigit);
			number /= 10;
		}
		lst.add(number);
		Collections.reverse(lst);
		return lst;
	}
}
