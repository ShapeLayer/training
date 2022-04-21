// 교재 6번 문제
import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("1~99 사이의 정수를 입력하시오 >> ");
    int gets = sc.nextInt();
    int cnt = 0;
    if (gets != 0 && (gets % 10) % 3 == 0) cnt += 1;
    System.out.println(gets);
    if ((gets / 10) != 0 && (gets / 10) % 3 == 0) cnt += 1;
    System.out.println("박수" + "짝".repeat(cnt));
  }
}