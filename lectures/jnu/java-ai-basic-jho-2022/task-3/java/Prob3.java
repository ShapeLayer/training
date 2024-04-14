/**
 * @author @ShapeLayer
 */

import java.util.Scanner;
// 예외 처리를 위해 InputMismatchException 클래스 임포트
import java.util.InputMismatchException;

public class Main {
  public static void main(String[] args) {
    int n, m;

    // 문제 제시 코드
    Scanner scanner = new Scanner(System.in);
    while (true) {
      System.out.print("곱하고자 하는 두수 입력>>");

      // 예외 처리를 위해 try-catch문 사용
      try {
        n = scanner.nextInt();
        m = scanner.nextInt();
        break;
      } catch (InputMismatchException e) {
        // `InputMismatchException` 오류를 캐치하도록 지정.
        // e는 오류(error) 정보를 담고 있음
        System.out.println("실수는 입력하면 안됩니다.");
        scanner.nextLine();
      }
    }
    System.out.println(n + "x" + m + "=" + n*m);
    scanner.close();
  }
}