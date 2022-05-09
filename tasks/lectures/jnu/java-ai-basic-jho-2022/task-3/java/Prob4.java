/**
 * @author @ShapeLayer
 */

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    // 표준 입력을 위해 Scanner 객체 선언
    Scanner sc = new Scanner(System.in);
    String gets;

    // 문제 제시 값
    String str[] = {"가위", "바위", "보"};

    System.out.println("컴퓨터와 가위 바위 보 게임을 합니다.");
    // "그만"이 입력될때까지 반복해야하므로 무한 루프 선언
    while (true) {
      System.out.print("가위 바위 보! >> ");
      gets = sc.next();
      // 문제 제시 코드
      int n = (int)(Math.random()*3);
      
      // "그만"이 입력된다면 무한 루프 종료
      if (gets.equals("그만")) break;

      // 문제에서 gets.equals()를 사용하여 값을 확인하라고 지정하였으니 아래와 같이 케이스별로 처리
      if (str[n].equals("가위")) {
        if (gets.equals("가위")) 
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 비겼습니다.", gets, str[n]));
        if (gets.equals("바위"))
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 사용자가 이겼습니다.", gets, str[n]));
        if (gets.equals("보"))
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 컴퓨터가 이겼습니다.", gets, str[n]));
      }
      else if (str[n].equals("바위")) {
        if (gets.equals("가위")) 
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 컴퓨터가 이겼습니다.", gets, str[n]));
        if (gets.equals("바위"))
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 비겼습니다.", gets, str[n]));
        if (gets.equals("보"))
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 사용자가 이겼습니다.", gets, str[n]));
      }
      else if (str[n].equals("보")) {
        if (gets.equals("가위")) 
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 사용자가 이겼습니다.", gets, str[n]));
        if (gets.equals("바위"))
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 컴퓨터가 이겼습니다.", gets, str[n]));
        if (gets.equals("보"))
          System.out.println(String.format("사용자 = %s, 컴퓨터 %s, 비겼습니다.", gets, str[n]));
      }
      // fallback
      //  "가위", "바위", "보" 외의 값을 입력했을 때 처리는 제시하지 않았으므로
      //  별도의 처리를 거치지 않고 루프를 계속함 (= 계속해서 입력을 받아옴)
    }
    System.out.println("게임을 종료합니다.");
  }
}