/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

import java.util.Scanner;

/**
 * DicApp 클래스
 * 
 * DicApp은 사전 애플리케이션 클래스입니다.
 * 사용자는 사전을 로드하여 사전에 기록되어 있는 단어를 검색할 수 있습니다.
 */
public class DicApp {
  /**
   * 단어가 한글 자모로 구성될 때 마지막 글자에 종성이 존재하는지 확인합니다.
   * 
   * @param word 확인할 단어
   * @return 마지막 글자에 종성이 존재하는지 여부
   */
  public static boolean isComplete(String word) {
    char lastWord = word.charAt(word.length() - 1);
    // 마지막 글자가 한국어가 아닌 경우 `false` 리턴
    if (lastWord < 0xAC00 || lastWord > 0xD7A3) { return false; }
    // 한글 자모를 분리하여 종성이 존재하는지 확인
    // 참조 https://hanpsy.tistory.com/2
    return (lastWord - 0xAC00) % 28 > 0; // 0인 경우 = 종성 데이터 없음 (= 종성 없음)
  }

  /**
   * 프로그램 진입점
   * @param args
   */
  public static void main(String[] args) {
    System.out.println("한영 단어 검색 프로그램입니다.");
    Scanner sc = new Scanner(System.in);

    // "종료"가 입력될 때까지 프로그램이 작동해야하므로 무한 루프 시작
    while (true) {
      System.out.print("한글 단어? ");
      String gets = sc.next();
      // "종료" 입력시 무한 루프 종료
      if (gets.equals("종료")) break;

      // Dictionary.kor2Eng 메서드는 정적 메서드이므로 객체를 생성하지 않고 호출
      // 결과가 있다면 String형으로 반환, 없다면 null 반환
      String res = Dictionary.kor2Eng(gets);
      System.out.println(String.format("%s%s %s",
        gets,
        DicApp.isComplete(gets) ? "은" : "는", // 은/는 여부 확인 메서드 호출. 종성이 있다면 "은", 없다면 "는"
        res != null ? res : "저의 사전에 없습니다." // kor2Eng 결과가 null이 아니라면 그대로 출력, null이라면 결과 없음 출력
      ));
    }
    System.out.println("프로그램을 종료합니다.");
  }
}

/**
 * Dictionary 클래스
 * 
 * Dictionary 클래스는 특정 문구를 키 값 삼아 대응되는 다른 문구로 변경할 수 있는 메서드를 제공합니다.
 */
class Dictionary {
  // 문제 제시 코드
  /**
   * 한국어 단어를 기록합니다.
   */
  private static String[] kor = {"사랑", "아기", "돈", "미래", "희망"};
  /**
   * 영어 단어를 기록합니다.
   */
  private static String[] eng = {"love", "baby", "money", "future", "hope"};

  /**
   * 입력받은 한국어 단어를 영어 단어로 반환합니다.
   * 만약 목록에 등록되어있지 않은 단어라면 {@code null}을 반환합니다.
   * 
   * @param word
   * @return {@code String?} 영단어 조회 결과를 반환합니다.
   */
  public static String kor2Eng(String word) {
    // 시간 복잡도 O(n)의 처리 알고리즘 구현
    for (int i = 0; i < kor.length; i++) {
      // 만약 `word`(메서드의 매개변수)가 배열에 있다면 변환 결과 리턴
      if (kor[i].equals(word)) {
        return eng[i];
      }
    }
    
    // 이 부분까지 도달했다면 단어 목록에 대상 단어가 존재하지 않음을 의미함
    // 단어가 존재하지 않으므로 null 반환
    return null;
  }
}