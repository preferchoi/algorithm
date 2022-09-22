package swexpertacademy.D1;

public class D1_2027 {
    public static void main(String[] args) {
    
            for (int i = 0; i < 5; i++) {
                for (int j = 0; j < i; j++) {
                    System.out.print("+");
                }
                System.out.print("#");
                for (int j = 4; j > i; j--) {
                    System.out.print("+");
                }
                System.out.println("");
    
            }
    
        }
    
    }
    