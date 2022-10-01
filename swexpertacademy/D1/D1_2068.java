package swexpertacademy.D1;

import java.util.Scanner;

public class D1_2068 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int test_case = 1; test_case <= T; test_case++) {

			int max = 0;
			for (int i = 0; i < 10; i++) {
				int num = sc.nextInt();
				if (max < num) {
					max = num;
				}
			}
			System.out.println("#" + test_case + " " + max);
		}
	}
}