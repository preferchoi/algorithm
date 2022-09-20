package swexpertacademy.D1;

import java.util.Scanner;

public class D1_2019 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int out = 1;
		for (int i = 0; i < num; i++) {
			if (i==0) {
				System.out.print("1 ");
			}
			out*=2;
			System.out.print(out+" ");
		}
	}

}