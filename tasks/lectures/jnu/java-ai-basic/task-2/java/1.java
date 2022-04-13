import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int gets = -1; // do-while문을 사용하지 않는 대신 음수로 초기화
    Scanner sc = new Scanner(System.in);
    System.out.print("양의 정수를 입력하시오: ");
    while (gets <= 0) { // 양의 정수가 입력될 때까지 반복
      gets = sc.nextInt();
      if (gets > 0) break; // 입력값이 양수이면 아래 라인을 수행하지 않고 반복 종료
      System.out.print("양의 정수가 아닙니다. 다시 입력하세요: ");
    }
    System.out.println(); // 개행
    // 출력 내용을 덜 복잡하게 확인할 수 있도록 문자열 포매팅 수행
    System.out.println(String.format("%d의 약수는 다음과 같습니다.", gets));

    // 가장 러프한 형태의 약수 알고리즘 구현
    // 시간복잡도: O(n)
    for (int i = 1; i <= gets; i++) {
      if (gets % i == 0) System.out.print(String.format("%d ", i));
    }

    // 터미널 환경에서 프로세스를 실행하면
    // 종료 시 개행되어야 다음 터미널 명령을 깔끔하게 입력할 수 있음.
    System.out.println();
  }
}