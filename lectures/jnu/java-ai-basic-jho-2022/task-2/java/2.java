import java.util.Scanner;

public class Main {
  public static boolean primes[];
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

    // 에라토스테네스의 체
    // 시간복잡도: O(n log log n)
    primes = new boolean[gets+1]; // gets까지 인덱싱할 수 있도록 gets+1 크기의 부울 배열 생성
    for (int i = 0; i < gets+1; i++) primes[i] = true; // 부울 배열 기본 초기값은 false이므로 true로 초기화
    primes[0] = false; primes[1] = false; // 0과 1은 소수가 아님
    System.out.print("결과: ");
    for (int i = 2; i < gets+1; i++) {
      if (primes[i]) { // 만약 primes[i]가 true라면 i가 소수임을 의미함
        System.out.print(String.format("%d ", i));
        for (int j = i; j < gets+1; j+=i) primes[j] = false; // i의 배수를 전부 false(합성수)로 처리
      }
    }

    // 터미널 환경에서 프로세스를 실행하면
    // 종료 시 개행되어야 다음 터미널 명령을 깔끔하게 입력할 수 있음.
    System.out.println();
  }
}