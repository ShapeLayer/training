/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

public class Main {
  public static void main(String[] args) {
    // 문제 제시 코드
    ColorPoint zeroPoint = new ColorPoint(); // (0,0) 위치의 BLACK 색점
    System.out.println(zeroPoint.toString() + "입니다.");
    ColorPoint cp = new ColorPoint(10, 10); // (10,10) 위치의 BLACK 색점
    cp.setXY(5, 5);
    cp.setColor("RED");
    System.out.println(cp.toString() + "입니다.");
  }
}

/**
 * Point 클래스
 * 
 * Point 클래스는 2차원 상의 한 점을 표현하는데 활용되는 클래스입니다.
 */
class Point {
  /**
   * 점의 x, y좌표입니다.
   */
  private int x, y;

  /**
   * Point 객체를 생성합니다.
   * @param x x좌표
   * @param y y좌표
   */
  public Point(int x, int y) { this.x = x; this.y = y; }

  /**
   * x좌표를 반환합니다.
   * @return {@code int} 점의 x좌표
   */
  public int getX() { return x; }
  
  /**
   * y좌표를 반환합니다.
   * @return {@code int} 점의 y좌표
   */
  public int getY() { return y; }

  /**
   * 점의 x좌표와 y좌표를 이동시킵니다. (= setter)
   * @param x 새 x좌표
   * @param y 새 y좌표
   */
  protected void move(int x, int y) { this.x = x; this.y = y; }
}

/**
 * ColorPoint 클래스
 * 
 * Point 클래스를 상속함
 * ColorPoint 클래스는 색상을 갖고 있는 한 점을 표현하는데 활용되는 클래스입니다.
 */
class ColorPoint extends Point {
  /**
   * 점의 색상, 기본값은 {@code "BLACK"}입니다.
   */
  private String color = "BLACK";

  /**
   * ColorPoint 객체를 생성합니다.
   * 생성된 객체의 x, y좌표는 (0, 0)입니다.
   */
  public ColorPoint() { this(0, 0); }
  /**
   * ColorPoint 객체를 생성합니다.
   * @param x x좌표
   * @param y y좌표
   */
  public ColorPoint(int x, int y) { super(x, y); }

  /**
   * 객체의 x좌표와 y좌표를 설정합니다. (= setter)
   * @param x x좌표
   * @param y y좌표
   */
  public void setXY(int x, int y) { this.move(x, y); }

  /**
   * 객체의 색상을 설정합니다. (= setter)
   * @param color 색상
   */
  public void setColor(String color) { this.color = color; }

  /**
   * 객체의 정보를 String형으로 변환해 반환합니다.
   * @return {@code String} 객체의 정보
   */
  public String toString() { return String.format("%s색의 (%d, %d)의 점", this.color, this.getX(), this.getY()); }
}