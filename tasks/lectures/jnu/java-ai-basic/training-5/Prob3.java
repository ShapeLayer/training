import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("소문자 알파벳 하나를 입력하시오 >> ");
    char gets = sc.next().charAt(0);
    for (int i = gets; i >= 97; i--) {
      for (int j = 97; j <= i; j++) {
        System.out.print((char)j);
      }
      System.out.println("");
    }
  }
}