import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    // 문제 제시 값
    int n = (int)(Math.random()*50.0);
    int tries = 0; // 시도 횟수 기록
    while (true) { // 무한 루프
      tries++;
      System.out.print("숫자를 추측하여 보세요: ");
      int gets = sc.nextInt(); // 입력
      if (gets < n) System.out.println("UP");
      else if (gets > n) System.out.println("DOWN");
      else {
        // 정답일 경우 시도 횟수를 출력하고 반복문 종료
        System.out.println(String.format("정답입니다. 시도횟수 = %d", tries));
        break;
      }
    }
  }
}