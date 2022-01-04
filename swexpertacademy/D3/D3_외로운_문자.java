package swexpertacademy.D3;

import java.util.Arrays;
import java.util.Scanner;

public class D3_외로운_문자 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for (int i = 1; i <= T; i++) {

            String test = sc.next();
            char[] a = new char[test.length()];
            for (int j = 0; j < test.length(); j++) {
                a[j] = test.charAt(j);
            }
        
            for (int j = 0; j < a.length; j++) {
                for (int j2 = 0; j2 < a.length; j2++) {
                    if (j!=j2 && a[j]==a[j2]) {
                        a[j]=0;
                        a[j2]=0;
                    }
                }
            }
            Arrays.sort(a);
            //답 도출부
            System.out.print("#"+i+" ");
            
            for (int j = 0; j < a.length; j++) {
                if (a[j]!=0) {
                    System.out.print(a[j]);
                }
            }
            int sum = 0;
            for (int j = 0; j < a.length; j++) {
                sum-=a[j];
            }
            if (sum>=0) {
                System.out.print("Good");
            }  
            System.out.println();
        }
    }
}