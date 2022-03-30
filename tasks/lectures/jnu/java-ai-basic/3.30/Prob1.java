import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("정수를 입력하시오 >> ");
    int n = sc.nextInt();
    for (int i = n; i > 0; i--) {
      System.out.println("*".repeat(i));
    }
  }
}