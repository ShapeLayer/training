/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

import java.util.Scanner;

/**
 * Phonebook 클래스
 * 
 * Phonebook 클래스는 주소록 애플리케이션 클래스입니다.
 * 사용자는 다른 사람들의 프로필을 등록하고, 등록한 프로필을 참조할 수 있습니다.
 */
public class Phonebook {
  /**
   * 프로그램 진입점
   * @param args
   */
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("인원수 >> ");

    // 인원수 입력 받아옴
    int n = sc.nextInt();
    // 입력값을 크기로 갖는 Phone 배열 생성
    Phone[] phones = new Phone[n];

    /* 프로필(전화번호부) 등록 프로세스 */
    // for문으로 배열의 요소들을 순차적으로 탐색
    // 사용자로부터 입력받고, 입력받은 값으로 초기화 진행
    for (int i = 0; i < n; i++) {
      System.out.print("이름과 전화번호 (이름과 번호는 빈 칸없이 입력)>> ");
      String name = sc.next();
      String tel = sc.next();
      // Phone 배열의 i번째 요소를 사용자의 입력값으로 초기화
      phones[i] = new Phone(name, tel);
    }
    System.out.println("저장되었습니다…");

    // "그만"이 입력될 때까지 계속해서 검색해야하므로 무한 루프 시작
    while (true) {
      System.out.print("검색할 이름 >> ");
      String gets = sc.next();

      // 입력값이 "그만"이라면 루프 종료
      if (gets.equals("그만")) break;

      // 검색 결과를 잘 찾아내고 출력했는지 확인하기위해 `flag` 변수 선언
      // 선언 시기에는 아직 검색을 시작하지 않았으므로 false로 설정
      boolean flag = false;

      // 검색 시작
      for (int i = 0; i < n; i++) {
        if (phones[i].getName().equals(gets)) {
          // 검색 결과가 존재하므로 `flag`를 true로 지정
          flag = true;
          // 결과 출력
          System.out.println(String.format("%s의 번호는 %s입니다.", phones[i].getName(), phones[i].getTel()));
        }
      }
      // `flag`가 `false`라면 검색 결과가 존재하지 않았다는 것이므로 fallback 처리
      // 문제에서 제시한 에제에서 "이(가) 없습니다."로 출력함
      if (!flag) { System.out.println(String.format("%s 이(가) 없습니다.", gets)); }
    }
    System.out.println("프로그램을 종료합니다.");
  }
}

/**
 * Phone 클래스
 * 
 * Phone 클래스는 Phonebook 클래스가 관리하는 프로필 단위입니다.
 * 하나의 프로필은 하나의 Phone 객체입니다.
 */
class Phone {
  /**
   * 대상의 이름입니다.
   */
  private String name;
  /**
   * 대상의 전화번호 정보입니다.
   */
  private String tel;

  /**
   * Phone 객체를 생성합니다.
   * @param name 대상의 이름
   * @param tel 대상의 전화번호
   */
  public Phone(String name, String tel) {
    this.name = name; this.tel = tel;
  }
  
  /**
   * {@code getter} 이름을 반환합니다.
   * @return {@code String} 이름
   */
  public String getName() { return name; }

  /**
   * {@code getter} 전화번호를 반환합니다.
   * @return {@code String} 전화번호
   */
  public String getTel() { return tel; }
}
