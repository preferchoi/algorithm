package swexpertacademy.D1;
import java.util.Scanner;

public class D1_2056 {
	public static void main(String args[]) throws Exception {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			int input = sc.nextInt();

			int yyyy = input / 10000;
			int mm = (input - yyyy * 10000) / 100;
			int dd = input - yyyy * 10000 - mm * 100;

			String out = "-1";

			if (yyyy < 1) {
				out = "-1";
			} else if (mm >= 1 && mm <= 12) {
				if (mm == 2) {
					out = yyyy + "/0" + mm;
					if (dd >= 1 && dd <= 9) {
						out += "/0" + dd;
					} else if (dd >= 10 && dd <= 28) {
						out += "/" + dd;
					} else {
						out = "-1";
					}
				} else if (mm == 1 || mm == 3 || mm == 5 || mm == 7 || mm == 8) {
					if (dd >= 1 && dd <= 31) {
						out = yyyy + "/0" + mm;
						if (dd >= 1 && dd <= 9) {
							out += "/0" + dd;
						} else if (dd >= 10 && dd <= 31) {
							out += "/" + dd;
						} else {
							out = "-1";
						}
					} else {
						out = "-1";
					}
				} else if (mm == 4 || mm == 6 || mm == 9) {
					if (dd >= 1 && dd <= 30) {
						out = yyyy + "/0" + mm;
						if (dd >= 1 && dd <= 9) {
							out += "/0" + dd;
						} else if (dd >= 10 && dd <= 30) {
							out += "/" + dd;
						} else {
							out = "-1";
						}
					} else {
						out = "-1";
					}
				} else if (mm == 10 || mm == 12) {
					if (dd >= 1 && dd <= 31) {
						out = yyyy + "/" + mm;
						if (dd >= 1 && dd <= 9) {
							out += "/0" + dd;
						} else if (dd >= 10 && dd <= 31) {
							out += "/" + dd;
						} else {
							out = "-1";
						}
					} else {
						out = "-1";
					}
				} else if (mm == 11) {
					if (dd >= 1 && dd <= 30) {
						out = yyyy + "/" + mm;
						if (dd >= 1 && dd <= 9) {
							out += "/0" + dd;
						} else if (dd >= 10 && dd <= 30) {
							out += "/" + dd;
						} else {
							out = "-1";
						}
					} else {
						out = "-1";
					}
				} else {
					out = "-1";
				}
			}else {
				out = "-1";
			}

			if (yyyy / 10 < 1) {
				out = "000" + out;
			} else if (yyyy / 100 < 1) {
				out = "00" + out;
			} else if (yyyy / 1000 < 1) {
				out = "0" + out;
			}

			System.out.println("#" + test_case + " " + out);

		}
	}
}