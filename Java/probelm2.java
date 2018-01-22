
public class euler2 {

	public static void main(String[] args) {
		
		int i = 0;
		long sum = 0;
		
		while (fib(i) < 4000000){
			if(fib(i) % 2 == 0) {
				sum += fib(i);	
			}
			
			i++;
		}
		
		System.out.println(sum);
		
		}
	
	public static int fib(int n){
		if(n == 1 || n == 0) {
			return 1;
		}else {
			return fib(n-1) + fib(n-2);
		}

	}

}
