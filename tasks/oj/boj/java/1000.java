/*
  [Java] 표준입력 STDIN
  https://noritersand.github.io/java/java-%ED%91%9C%EC%A4%80%EC%9E%85%EB%A0%A5-stdin/
*/
import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt();
    int b = in.nextInt();
    // in.close();
    System.out.println(a+b);
  }
}