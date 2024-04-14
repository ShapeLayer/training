/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    // 문제 제시 코드
    Scanner scanner = new Scanner(System.in);
    System.out.print("수학, 과학, 영어순으로 3개의 점수 입력>>");
    int math = scanner.nextInt();
    int science = scanner.nextInt();
    int english = scanner.nextInt();
    Grade me = new Grade(math, science, english);
    System.out.println("평균은 " + me.average());
    // average()는 평균을 계산하여 리턴
    scanner.close();
  }
}

/**
 * Grade 클래스
 * Grade 클래스는 수학, 과학, 영어 세 과목의 점수를 처리할 수 있는 클래스입니다.
 * 세 과목을 한 번에 관리할 수 있고, 세 과목의 평균을 쉽게 확인할 수 있도록 지원합니다.
 */
class Grade {
  // 자바에서 접근 제어자는 기본값이 private이므로 접근 제어자를 생략하면 기본값 private로 지정됨

  /**
   * 수학 과목 점수
   */
  int math;

  /**
   * 과학 과목 점수
   */
  int science;

  /**
   * 영어 과목 점수
   */
  int english;

  /**
   * Grade 객체를 생성합니다.
   * @param math 수학 과목 점수
   * @param science 과학 과목 점수
   * @param english 영여 과목 점수
   */
  public Grade(int math, int science, int english) {
    this.math = math;
    this.science = science;
    this.english = english;
  }

  /**
   * 수학 과학 영어 세 과목의 평균값을 정수로 반환합니다.
   * @return {@code int} 세 과목의 평균값
   */
  int average() {
    return (this.math + this.science + this.english) / 3;
  }
}