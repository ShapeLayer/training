/**
 * @author @ShapeLayer
 */

/*
  Average.java
  CLI 환경에서 실행하고자 한다면 `java Average.java 1 2 3 5 7 8 1 2 3 4`를 입력하세요.
*/

public class Main {
  public static void main(String[] args) {
    int sums = 0; // 합계 기록할 변수 선언
    // `args` 변수의 길이만큼 반복문 시작
    for (int i = 0; i < args.length; i++) {
      // `args[i]`는 String형 값이므로 int형으로 캐스팅한 뒤 `sums`에 가산
      sums += Integer.parseInt(args[i]);
    }
    // `sums`와 `args.length` 모두 정수이므로 둘 중 하나를 실수로 캐스팅해야 실수 계산이 수행됨
    // 실수로 캐스팅하지않으면 몫 연산 수행
    System.out.println("입력받은 인자 값의 평균은 : " + sums/(float)args.length);
  }
}