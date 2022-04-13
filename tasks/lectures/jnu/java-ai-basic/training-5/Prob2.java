import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("정수를 입력하시오 >> ");
    int n = sc.nextInt();
    // n만큼 반복
    for (int i = 0; i < n; i++) {
      System.out.println("*".repeat(2*i+1)); // 별이 2*i+1회 찍혀야함 (i = 반복 횟수, 0부터 시작)
      // for (int j = 0; j < 2*i+1; j++) System.out.print("*");
      // System.out.println();
    }
  }
}