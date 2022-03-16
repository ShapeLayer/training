import java.util.Scanner;
public class Prob3 {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("원화를 입력하세요 (단위 원) >> ");
    int gets = sc.nextInt();
    System.out.println(gets + "원은 $" + (double)gets/1100 + "입니다.");
  }
}