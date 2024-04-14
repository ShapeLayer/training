/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

public class Main {
  public static void main(String [] args) {
    IPTV iptv = new IPTV("192.1.1.2", 32, 2048);
    iptv.printProperty();
  }
}

/**
 * TV 클래스
 * 
 * TV 클래스는 생산된 TV에 대한 정보를 담습니다.
 */
class TV {
  /**
   * TV의 크기(인치)입니다.
   */
  private int size;

  /**
   * TV 객체를 생성합니다.
   * @param size 크기(인치)
   */
  public TV (int size) { this.size = size; }

  /**
   * TV의 크기를 반환합니다.
   * @return {@code int} TV의 크기(인치)
   */
  protected int getSize() { return size; }
}

/**
 * ColorTV 클래스
 * 
 * TV 클래스를 상속함
 * ColorTV 클래스는 생산된 컬러TV에 대한 정보를 담습니다.
 */
class ColorTV extends TV {
  /**
   * TV가 표현할 수 있는 색상의 정보입니다.
   */
  private int colors;

  /**
   * ColorTV 객체를 생성합니다.
   * @param size {@code int} 크기(인치)
   * @param colors {@code int} 표현 가능한 색상 수
   */
  public ColorTV (int size, int colors) {
    super(size);
    this.colors = colors;
  }

  /**
   * TV가 표현 가능한 색상의 개수를 반환합니다.
   * @return {@code int} 표현 가능한 색상 수
   */
  protected int getColors() {
    return this.colors;
  }
  
  /**
   * TV의 속성을 표준 출력합니다.
   */
  public void printProperty() {
    System.out.println(String.format("%d인치 %d컬러", this.getSize(), this.getColors()));
  }
}

/**
 * IPTV 클래스
 * 
 * ColorTV를 상속함
 * IPTV 클래스는 생산된 IPTV에 대한 정보를 담습니다.
 */
class IPTV extends ColorTV {
  /**
   * TV의 IP주소
   */
  private String ip;

  /**
   * IPTV 객체를 생성합니다.
   * @param ip {@code String} IP주소
   * @param size {@code int} 크기(인치)
   * @param colors {@code int} 표현 가능한 색상 수
   */
  IPTV(String ip, int size, int colors) {
    super(size, colors);
    this.ip = ip;
  }

  /**
   * TV에 할당된 IP 주소를 반환합니다.
   * @return {@code String} IP 주소
   */
  protected String getIP() { return this.ip; }

  /**
   * TV의 속성을 표준 출력합니다.
   */
  public void printProperty() {
    System.out.println("나의 IPTV는 "+this.getIP()+" 주소의 "+this.getSize()+"인치 "+this.getColors()+"컬러");
  }
}