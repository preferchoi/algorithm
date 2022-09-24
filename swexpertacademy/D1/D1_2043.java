package swexpertacademy.D1;

import java.util.Scanner;

public class D1_2043 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int p = sc.nextInt();
		int k = sc.nextInt();
		int count = 0;

		while (k<=p) {
			k++;
			count++;
		}
		System.out.println(count);
	}

}