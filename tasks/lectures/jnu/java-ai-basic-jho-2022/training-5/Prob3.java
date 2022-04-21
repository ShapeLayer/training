import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("소문자 알파벳 하나를 입력하시오 >> ");
    // charAt 메서드는 인자로 받아오는 인덱스 번호를 통해 문자열을 인덱싱할 수 있도록 함
    // (= String 형 값을 char 값으로 캐스팅)
    char gets = sc.next().charAt(0);
    // 'a'는 97임, gets에서 시작하여 'a'까지 반복
    for (int i = gets; i >= 97; i--) { 
      // 각 열마다 알파벳 출력
      for (int j = 97; j <= i; j++) {
        System.out.print((char)j);
      }
      System.out.println(); // 개행
    }
  }
}