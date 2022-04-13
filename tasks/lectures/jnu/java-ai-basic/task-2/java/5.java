import java.util.Scanner;

public class Main {
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);
    
    // 문제 제시 값 
    int[] unit = {50000, 10000, 1000, 500, 100, 50, 10};

    // 잔액 변수 생성
    int remains = -1;
    System.out.print("금액을 입력하시오 >> ");
    remains = sc.nextInt();
    for (int u: unit) { // foreach문 사용, u는 unit의 요소(단위)
      int n = remains / u; // 잔액을 단위로 나눈 몫 구하기 (=지폐 혹은 화폐의 개수)
      if (n == 0) continue; // 몫이 0이면 다음 단위 처리
      System.out.println(String.format("%d원: %d개", u, n));
      remains -= u*n;
    }
  }
}