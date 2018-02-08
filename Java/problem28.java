
public class problem28 {

	public static void main(String[] args) {

		System.out.println(Spiral(500));
	}

	//f(0) = 1

	//nxt num

	// f(n) = (2n+1)^2 - 2n

	//n = 1
	//1, 3, 5, 7, 9 = 25

	//n = 2
	//1, 3, 5, 7, 9, 13, 17, 21, 25 = 101

	//...

	//sum of all corners

	//n = 1: 3, 5, 7, 9 = 24
	//n = 2: 13, 17, 21, 25 = 76

	// f(n) = 4(2n + 1)^2 - 12n

	//sum of spiral

	//f(n) = 4(2n + 1)^2 - 12n + f(n-21), f(0) = 1

	public static int Spiral(int n) {
		if(n == 0) {
			return 1;
		}
		return 4*((2*n + 1)* (2*n + 1)) - 12*n + Spiral(n-1);
	}
}
