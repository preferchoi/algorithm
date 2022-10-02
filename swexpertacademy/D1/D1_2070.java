package swexpertacademy.D1;

import java.util.Scanner;

public class D1_2070 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int i = 1; i <= T; i++) {

			int num1 = sc.nextInt();
			int num2 = sc.nextInt();
			
			if (num1>num2) {
				System.out.println("#"+i+" >");
			}else if (num1<num2) {
				System.out.println("#"+i+" <");
			}else {
				System.out.println("#"+i+" =");
			}

		}
	}

}
