
public class problem53 {

	public static void main(String[] args) {
		
		//System.out.println(nCr(23,10));
		//System.out.println(fac(13) * fac(10));
		//System.out.println(fac(23));
		
	}

	public static long nCr(long n, long r) {
		if(n == r) {
			return 1;
		}
		if(r > n) {
			return 0;
		}
		System.out.println("n: "+n+" n-r: "+ (n-r)+" r; "+r);
		long div = (fac(n-r) * fac(r));
		return fac(n) / div;
	}
	
	public static long fac(long n) {
		if (n == 0) {
			return 1;
		}
		else {
			return n * fac(n-1);
		}
	}
}
