/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    // 문제 제시 코드
    TV myTV = new TV("LG", 2017, 32);
    myTV.show();
  }
}

/**
 * TV 클래스
 *
 * TV 클래스는 생산된 TV에 대한 정보를 담을 수 있습니다.  
 * 이름, 생산자(생산업체), 인치 정보를 담고 처리할 수 있고, 그 내용을 출력할 수 있습니다.
 */
class TV {
  /**
   * TV 이름을 표현합니다.
   */
  String name;

  /**
   * 생산자(생산업체)를 표현합니다.
   */
  int manufactures;

  /**
   * 크기를 인치 단위로 표현합니다.
   */
  int inch;

  /**
   * TV 객체를 생성합니다.
   * 
   * @param name TV의 이름
   * @param manufactures 생산자(생산업체)
   * @param inch 크기(인치)
   */
  public TV(String name, int manufactures, int inch) {
    // `this.name`은 TV 객체의 name 속성, `name`은 생성자의 매개변수
    // 아래와 같이 작성한다면 생성자의 매개변수를 객체의 각 속성으로 저장할 수 있음
    this.name = name;
    this.manufactures = manufactures;
    this.inch = inch;
  }

  /**
   * TV 정보를 콘솔에 표준 출력합니다.
   * 
   * @return {@code null}
   */
  public void show() {
    System.out.println(String.format("%s에서 만든 %d년형 %d인치 TV", this.name, this.manufactures, this.inch));
  }
}