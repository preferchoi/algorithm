package swexpertacademy.D1;

import java.util.Scanner;

public class D1_2050 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String a = sc.next();
		int b = 0;
		while (a.length()>b) {
			System.out.print((int)a.charAt(b)-64+" ");
			b++;
		}
	}

}
