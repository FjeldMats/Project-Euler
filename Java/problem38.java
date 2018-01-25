import java.util.ArrayList;
import java.util.Collections;

public class problem38 {

	public static void main(String[] args) {
		
		
		long num = 1;
		long pandigitalNum = 1;
		int inc = 0;
		int n = 1;
		
		for(int i = 0; i<1000000;i++) {
			num = 1 + i;
			pandigitalNum = 1 + i;
			inc = 0;
			n = 1;
			boolean first = true;
			while(pandigitalNum < 987654321){
				if(first) {
					n++;
					first = false;
					continue;
				}
				
				if(LongLength(pandigitalNum) <= 9){
					pandigitalNum = concatIntegers(pandigitalNum,n*num);
					n++;
					//System.out.println(pandigitalNum);
				}else {
					inc++;
					pandigitalNum = inc;
					n = 1;
				}
				
				if(isPandigital(pandigitalNum) && LongLength(pandigitalNum) == 9) {
					System.out.println(pandigitalNum);
					
				}
			}
	}
		
	}
	
	public static boolean isPandigital(long number) {
		ArrayList<Integer> allNums = new ArrayList<Integer>();
		ArrayList<Integer> numsList = integerToArray(number);
		
		for(int i = 1;i<10;i++) {
			allNums.add(i);
		}
		for(int j = 0; j < numsList.size(); j++) {
			for(int n = 0;n<allNums.size(); n++) {
				if(numsList.get(j) == allNums.get(n)) {
					allNums.remove(new Integer(numsList.get(j)));
					break;
				}
			}
		}
		//System.out.println(allNums + " " + numsList);
		if(allNums.isEmpty()) {
			return true;
		}
		
		return false;
	}
	
	public static ArrayList<Integer> integerToArray(long number){
		ArrayList<Integer> lst = new ArrayList<Integer>();
		while (number>10) {
			long lastDigit = number%10;
			lst.add((int) lastDigit);
			number /= 10;
		}
		if(number != 10) {
			lst.add((int) number);
		}else {
			lst.add(1);
			lst.add(0);
		}
		
		Collections.reverse(lst);
		return lst;
	}
	
	public static long concatIntegers(long num1, long num2) {
		ArrayList<Integer> nums1 = integerToArray(num1);
		ArrayList<Integer> nums2 = integerToArray(num2);
		
		for(int i=0;i<nums2.size();i++) {
			nums1.add(nums2.get(i));
		}
		
		String numAsString = new String();
		
		for(int j=0;j<nums1.size();j++) {
			numAsString += Integer.toString(nums1.get(j));
		}
		
		return Long.parseLong(numAsString);
	}
	
	public static long LongLength(long num) {
		ArrayList<Integer> nums = integerToArray(num);
		return nums.size();
		
	}

}
