/**
 * @author @ShapeLayer
 */

// 문제 제시 코드
public class DictionaryApp {
  public static void main(String[] args) {
    Dictionary dic = new Dictionary(10);
    dic.put("황기태", "자바");
    dic.put("이재문", "파이선");
    dic.put("이재문", "C++");
    System.out.println("이재문의 값은 " + dic.get("이재문"));
    System.out.println("황기태의 값은 " + dic.get("황기태"));
    dic.delete("황기태");
    System.out.println("황기태의 값은 " + dic.get("황기태"));
  }
}

// 문제 제시 추상 클래스
abstract class PairMap {
  protected String keyArray [];
  protected String valueArray [];
  abstract String get(String key);
  abstract void put(String key, String value);
  abstract String delete(String key);
  abstract int length();
}

/**
 * Dictionary 클래스
 * {@code PairMap} 클래스 상속함
 * 
 * Dictionary 클래스는 해시맵(혹은 딕셔너리) 자료형의 구현체입니다.
 * Dictionary 클래스는 특정 키 값에 대해 정보를 저장하고, 다시 쉽게 불러올 수 있도록 돕는 메서드들이 포함되어 있습니다.
 */
class Dictionary extends PairMap {
  /**
   * 딕셔너리가 담을 수 있는 자료 개수입니다.
   */
  int size;
  /**
   * 딕셔너리에서 현재 유효한 값에 대한 정보입니다.
   * 만약 값이 사용 가능한 상태라면 {@code true}, 아니라면 {@code false}가 기록됩니다.
   */
  boolean availables[];

  /**
   * Dictionary 객체를 생성합니다.
   * @param size {@code int} 딕셔너리의 크기
   */
  public Dictionary(int size) {
    this.size = size;
    // 크기에 맞춰 배열들 초기화
    this.keyArray = new String[size];
    this.valueArray = new String[size];
    this.availables = new boolean[size];
  }

  /**
   * {@code getter}
   * 딕셔너리에 기록된 값을 찾습니다. 만약 기록된 내용이 없다면 {@code null}를 반환합니다.
   * @param {@code key} 딕셔너리를 인덱싱할 인덱스 키
   * @return {@code String?} 딕셔너리의 인덱싱 결과
   */
  @Override
  String get(String key) {
    // 배열 크기만큼 반복문 시작
    for (int i = 0; i < this.size; i++) {
      // 만약 i번째 값이 유효한 값이 아니라면 다음 인덱스 확인
      // 유효하지 않은 값: 초기화되지 않음, 삭제됨
      if (!this.availables[i]) continue;
      // 만약 i번째 값이 유효한 값이라면
      // 함수 매개변수로 주어진 key와 keyArray의 현재 인덱싱 결과가 같은지 확인
      if (key.equals(this.keyArray[i])) {
        // 결과가 같다면 값(value) 반환
        return this.valueArray[i];
      }
    }
    // 이 지점까지 도달했다면 반복문을 모두 통과하고도
    // key값이 딕셔너리에 없다는 의미이므로 null 반환
    return null;
  }

  /**
   * {@code setter}
   * 딕셔너리에 값을 기록합니다.
   * 만약 딕셔너리가 꽉 차있다면 경고를 출력하고 함수가 종료됩니다.
   * 만약 매개 변수로 주어진 키로 딕셔너리를 인덱싱할 수 있다면 딕셔너리 내의 해당 값이 덮어쓰기됩니다.
   * @param key {@code String} 딕셔너리 키
   * @param value {@code String} 딕셔너리 값
   */
  @Override
  void put(String key, String value) {
    // 만약 get의 호출 결과가 null이라면 딕셔너리에 존재하지 않는 값이라는 의미임
    if (this.get(key) == null) {
      // 반복 시작: 딕셔너리에 사용 가능한 공간이 있는지 확인
      for (int i = 0; i < this.size; i++) {
        // 만약 현재 인덱스가 유효하지 않은 값을 가지고 있다면
        // 사용 가능한 공간임을 의미함
        if (!this.availables[i]) {
          this.availables[i] = true; // 현재 인덱스를 유효함으로 플래그
          // 딕셔너리 값 업데이트
          this.keyArray[i] = key;
          this.valueArray[i] = value;
          // 함수 종료
          return;
        }
      }
      // 오류 메시지 출력 후 함수 종료
      System.out.println("Error: No more spaces");
      return;
    } else {
      // 만약 get의 호출 결과가 null이 아니라면 이미 해당 키 값이 이 딕셔너리에 대해 유효하다는 의미임
      // 반복문 시작
      for (int i = 0; i < this.size; i++) {
        // 유효하지 않은 값을 찾는 것이 아니므로 유효하지 않은 값은 스킵
        if (!this.availables[i]) continue;
        // 만약 i번째 값이 유효한 값이라면
        // 함수 매개변수로 주어진 key와 keyArray의 현재 인덱싱 결과가 같은지 확인
        if (key.equals(this.keyArray[i])) {
          // 덮어쓰기 대상이라면 덮어쓰기 후 함수 종료
          this.valueArray[i] = value;
          return;
        }
      }
    }
  }

  /**
   * 딕셔너리에서 값을 제거합니다.
   * @param key {@code String} 제거할 값의 키
   * @return {@code String} 제거한 값
   */
  @Override
  String delete(String key) {
    // 반복문 시작
    for (int i = 0; i < this.size; i++) {
      // 만약 현재 인덱스 결과가 유효하지 않은 값이라면 다음 인덱스 처리
      if (!this.availables[i]) continue;
      // 만약 key값을 찾았다면
      if (key.equals(this.keyArray[i])) {
        // 실제로 삭제하지는 않음. 해당 공간이 비어있다고 표기한 후 나중에 덮어쓰기함.
        this.availables[i] = false;
        return this.valueArray[i]; // 삭제한 값 반환
      }
    }
    return null;
  }

  /**
   * 딕셔너리에 기록된 유효한 값들의 개수를 반환합니다.
   * @return {@code int} 유효한 값들의 개수
   */
  @Override
  int length() {
    // 카운터 선언
    int ables = 0;
    // 반복문 시작
    for (int i = 0; i < this.size; i++) {
      // 만약 현재 인덱스 결과가 유효하다면 카운터 1 증가
      if (this.availables[i]) ables++;
    }
    return ables;
  }
}