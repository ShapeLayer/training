import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("정수를 입력하시오 >> ");
    int n = sc.nextInt(); // 입력
    for (int i = n; i > 0; i--) { // n회 반복
      System.out.println("*".repeat(i)); // repeat 메서드는 인자만큼 문자열 객체를 반복함
      // for (int j = 0; j < i; j++) System.out.print("*");
      // System.out.println();
    }
  }
}