/**
 * @author @ShapeLayer
 */

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    // 표준 입력을 위해 Scanner 객체 선언
    Scanner sc = new Scanner(System.in);

    // 문제 제시 값
    String course[] = {"java", "c++", "HTML5", "컴퓨터구조", "안드로이드"};
    int score[] = {95, 88, 76, 62, 55};
    String name;

    // 입력값이 "그만"일 때까지 프로그램이 작동해야하므로 무한 루프 시작
    while(true) {
      // 과목 이름 입력
      System.out.print("과목 이름 >> ");
      name = sc.next();

      // 입력값이 "그만"인 경우 프로그램 종료
      if (name.equals("그만")) { break; }

      // 검색 중 입력값에 해당하는 값이 존재하고 출력했는지 여부를 확인하기 위해
      // 부울형 `flag` 변수 선언
      // 아직 존재하는지 확인하지 않았고, 결과를 출력하지 않았으므로 false로 지정
      boolean flag = false;
      for (int i = 0; i < course.length; i++) {
        // 과제 첨부 파일의 "실행 예"에서 Java를 입력했는데 java의 결과가 출력되는 것을 확인할 수 있음
        // 따라서 이 프로그램은 대소문자를 구분하지 않는 것으로 처리함
        // * 입력값과 키(과목)값 모두 소문자로 변환한 후 두 값이 같은지 확인
        if (course[i].toLowerCase().equals(name.toLowerCase())) {
          System.out.println(String.format("%s의 점수는 %d", name, score[i]));
          flag = true; // 대상이 존재하므로 `flag`를 true로 변경
        }
      }
      // `flag`가 false라면 대상이 존재하지 않고 결과를 출력한 사실도 없으므로 없는 과목이라고 출력
      if (!flag) System.out.println("없는 과목입니다.");
    }
  }
}