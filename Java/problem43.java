import java.util.ArrayList;
import java.util.Collections;

public class problem43 {

	public static void main(String[] args) {
		
		int sumOfPan = 0;
		
		for(int i = 123456789; i < 987654321;i++) {
			
			if(i%10000000 == 0) {
				System.out.println(i + " / "+987654321);
			}
			
			if((isPandigital(i))) {
				
				ArrayList<Integer> nums = integerToArray(i);
				ArrayList<Integer> tempLst = new ArrayList<Integer>();
				
				for(int j = 0; j < 9; j++) {
					for(int k = 0; k < 3; k++) {
						tempLst.add(nums.get(j));
					}
					if(tempLst.size()>10) {
						continue;
					}
					int divNum = arrayToInteger(tempLst);
					if(divisibleBy(divNum) != -1) {
						//System.out.print(divNum + " ");
					}
					else {
						//System.out.println(divNum + " notDiv \n");
						break;
					}
					sumOfPan += i;
				}
				//System.out.print("\n");
			}
		}
		System.out.println(sumOfPan);
	}
	
	public static boolean isPandigital(int number) {
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
		if(allNums.isEmpty()) {
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
		if(number != 10) {
			lst.add(number);
		}else {
			lst.add(1);
			lst.add(0);
		}
		
		Collections.reverse(lst);
		return lst;
	}
	
	public static int divisibleBy(int num) {
		for(int i = 2;i<num;i++) {
			if(num % i == 0) {
				return i;
			}
		}
		return -1;
	}
	
	public static int arrayToInteger(ArrayList<Integer> list) {
		
		String numAsString = new String();
		
		for(int j=0;j<list.size();j++) {
			numAsString += Integer.toString(list.get(j));
		}
		
		return Integer.parseInt(numAsString);
		
	}

}
