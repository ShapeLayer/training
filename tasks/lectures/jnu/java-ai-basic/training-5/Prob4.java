import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int n = (int)(Math.random()*50.0);
    int tries = 0;
    while (true) {
      tries++;
      System.out.print("숫자를 추측하여 보세요: ");
      int gets = sc.nextInt();
      if (gets < n) System.out.println("UP");
      else if (gets > n) System.out.println("DOWN");
      else {
        System.out.println(String.format("정답입니다. 시도횟수 = %d", tries));
        break;
      }
    }
  }
}