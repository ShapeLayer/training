/**
 * @author @ShapeLayer
 */

import java.util.Collections;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n;
    String gets;
    StringStack stack;
    Scanner sc = new Scanner(System.in); // 스캐너 객체 생성
    System.out.print("총 스택 저장 공간의 크기 입력 >> ");
    n = sc.nextInt();
    // 아래에서 정의한 StringStack 객체 생성
    stack = new StringStack(n);

    int i = 0;
    // "그만"이 입력될 때까지 문자열을 받아와야하므로 무한 루프 시작
    while (true) {
      System.out.print("문자열 입력 >> ");
      gets = sc.next();
      // 만약 "그만"이 입력됐다면 루프 종료
      if (gets.equals("그만")) break;
      // 스택에 입력값을 푸시함과 동시에 결과를 받아와서 성공했는지 여부 확인
      if (!stack.push(gets)) { // 만약 실패했다면 알림 출력
        System.out.println("스택이 꽉 차서 푸시 불가!");
      }
    }
    System.out.println("스택에 저장된 모든 문자열 팝 : " + String.join(" ", stack.getData()));
  }
}

// 문제 제시 인터페이스
interface Stack {
  int length();
  int capacity();
  String pop();
  boolean push(String val);
}

/**
 * StringStack 클래스
 * {@code Stack} 클래스 상속
 * 
 * StringStack 클래스는 문자열 값을 스택 자료형으로 처리하는데 유용한 메서드가 포함되어 있습니다.
 */
class StringStack implements Stack {
  /**
   * 스택의 크기
   */
  int size
  /**
   * 스택의 가장 높은 값의 인덱스
   */
  int peek = -1;
  /**
   * 스택 데이터
   */
  String data[];

  /**
   * StringStack 객체를 생성합니다.
   * @param size {@code int} 스택의 크기
   */
  public StringStack(int size) {
    // 스택의 크기 기록 후 데이터 배열 초기화
    this.size = size;
    this.data = new String[this.size];
  }

  /**
   * 스택의 크기를 반환합니다.
   * @return {@code int} 스택의 크기
   */
  @Override
  public int length() { return this.size; }

  /**
   * 스택의 용량을 반환합니다.
   * @return {@code int} 스택의 용량
   */
  @Override
  // peek는 가장 높은 값의 인덱스를 기록하므로, 용량을 표현하려면 1을 더해야함
  public int capacity() { return peek+1; }

  /**
   * 스택에 값을 푸시합니다.
   * 만약 성공했다면 {@code true}, 실패했다면 {@code false}를 반환합니다.
   * @param push {@code String} 푸시할 값
   */
  @Override
  public boolean push(String val) {
    // 만약 스택의 가장 높은 값의 인덱스가 스택의 크기보다 작다면
    // 즉, 스택에 잔여 공간이 있다면
    if (this.peek < this.length()-1) {
      // 꼭대기 인덱스 값을 높이고 값 업데이트
      this.peek++;
      this.data[this.peek] = val;
      return true;
    } else {
      // 스택에 잔여 공간이 없다면 아무 일도 하지 않고 false 반환
      return false;
    }
  }

  /**
   * 스택으로부터 값을 팝합니다.
   * 만약 성공했다면 해당 값을 반환하고, 실패했다면 {@code null}을 반환합니다.
   * @return {@code String?} 팝 결과
   */
  @Override
  public String pop() {
    // 만약 꼭대기 인덱스가 -1이라면 빈 스택이라는 의미이므로 null 리턴
    if (this.peek < 0) return null;
    // 아니라면 꼭대기 인덱스를 1 줄이고 결과 반환
    // 값을 실제로 지우지는 않음: 새로 값을 푸시할 때 덮어쓰기함
    this.peek--;
    return this.data[this.peek+1];
  }

  /**
   * 모든 데이터를 팝 했을 때 결과를 반환합니다.
   * @return {@code String[]} 모든 데이터를 팝 했을 때 결과
   */
  public String[] getData() {
    String[] results = new String[this.length()];
    // 스택은 선입후출되므로, 데이터 배열을 그대로 반환하면 안됨
    // O(N) 시간복잡도의 배열 reverse 처리
    for (int i = 0; i < this.length(); i++) {
      results[i] = this.data[this.length()-1-i];
    }
    return results;
  }
}