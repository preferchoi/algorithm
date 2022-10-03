package swexpertacademy.D1;
import java.util.Scanner;

public class D1_2071 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int t = sc.nextInt(); // 반복 횟수
		double[] time = new double[t];
		for (int j = 1; j < t + 1; j++) { // t만큼 반복
			double sum = 0; // 여기에 홀수 더함, 반복할때마다 0으로 초기화
			double avg = 0;
			int[] ary = new int[10]; // 10칸짜리 배열 만들어줌
			for (int i = 0; i < ary.length; i++) { // 배열 길이만큼 반복
				ary[i] = sc.nextInt();// 만든 배열에 값 입력
			}
			for (int i = 0; i < ary.length; i++) {// 다 더하고
				sum += ary[i];
				if (i == ary.length - 1) {// 다 더했으면 평균구함
					avg = sum / ary.length;
				}
			}

			double half = avg * 10 - (int) avg * 10;// 소수점 첫째자리 자연수값으로 가져옴
			if (half - 5 < 0) {// 반올림해줌
				time[j - 1] = (int) avg;
			} else {
				time[j - 1] = (int) avg + 1;
			}
		}
		for (int i = 1; i <= time.length; i++) {
			System.out.println("#" + i + " " + (int) time[i - 1]);
		}
		sc.close();
	}
}


