import java.util.Scanner;
import java.util.InputMismatchException;

public class Main {
  public static void main(String[] args) {
    int n, m;
    // 문제 제시 코드
    Scanner scanner = new Scanner(System.in);
    while (true) {
      System.out.print("곱하고자 하는 두수 입력>>");
      try {
        n = scanner.nextInt();
        m = scanner.nextInt();
        break;
      } catch (InputMismatchException e) {
        System.out.println("실수는 입력하면 안됩니다.");
        scanner.nextLine();
      }
    }
    System.out.println(n + "x" + m + "=" + n*m);
    scanner.close();
  }
}