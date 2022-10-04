package swexpertacademy.D1;
import java.util.Scanner;
//https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq&categoryId=AV5QSEhaA5sDFAUq&categoryType=CODE
//10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
//[제약 사항]
//각 수는 0 이상 10000 이하의 정수이다.
public class D1_2072 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt(); // 반복 횟수
		int[] time = new int[t];
		for (int j = 1; j < t+1; j++) { // t만큼 반복
			int sum = 0; // 여기에 홀수 더함, 반복할때마다 0으로 초기화
			int[] ary = new int[10]; //10칸짜리 배열 만들어줌
			for (int i = 0; i < ary.length; i++) { //배열 길이만큼 반복
				ary[i] = sc.nextInt();//만든 배열에 값 입력
			}
			for (int i = 0; i < ary.length; i++) {
				if (ary[i] % 2 == 1) {//배열의 숫자가 홀수면 
					sum += ary[i];//더해서 모아줌
				}
				time[j-1]=sum;
			}
		}
		for (int i = 1; i <= time.length; i++) {
			System.out.println("#"+i+" "+time[i-1]);			
		}
		sc.close();
	}
}
