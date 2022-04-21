import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    System.out.print("제곱미터를 입력하세요 >> ");
    Scanner sc = new Scanner(System.in);
    int gets = sc.nextInt();
    System.out.println(gets + "m^2은 " + gets*0.305785 + "평 입니다.");
  }
}