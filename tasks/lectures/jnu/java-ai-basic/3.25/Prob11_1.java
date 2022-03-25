// 교재 11번 문제
import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("달을 입력하세요(1~12)>>");
    int month = sc.nextInt();
    if (month <= 2) System.out.println("겨울");
    else if (month <= 5) System.out.println("봄");
    else if (month <= 8) System.out.println("여름");
    else if (month <= 11) System.out.println("여름");
    else if (month <= 12) System.out.println("겨울");
    else System.out.println("잘못 입력");
  }
}