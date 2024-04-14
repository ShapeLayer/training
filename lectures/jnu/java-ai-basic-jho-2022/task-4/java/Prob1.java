/**
 * @author @ShapeLayer
 */

// 문제 제시 코드
public class Main {
  public static void main(String[] args) {
    PositivePoint p = new PositivePoint();
    p.move(10, 10);
    System.out.println(p.toString() + "입니다.");

    p.move(-5, -5);
    System.out.println(p.toString() + "입니다.");

    PositivePoint p2 = new PositivePoint(-10, -10);
    System.out.println(p2.toString() + "입니다.");
  }
}

// 문제 제시 코드
class Point {
  private int x, y;
  public Point(int x, int y) { this.x = x; this.y = y; }
  public int getX() { return x; }
  public int getY() { return y; }
  protected void move(int x, int y) { this.x = x; this.y = y; }
}

/**
 * PositivePoint 클래스
 *
 * PositivePoint 클래스는 2차원 상의 한 점 중 1사분면과, 1사분면에 인접한 축 위에 있는 점에 대해 표현합니다.
 */
public class PositivePoint extends Point {
  /**
   * PositivePoint 객체를 생성합니다.
   * @param {@coode void}
   */
  public PositivePoint() {
    super(0, 0);
  }

  /**
   * PositivePoint 객체를 생성합니다.
   * @param {@coode x} 점의 x좌표
   * @param {@coode y} 점의 y좌표
   */
  public PositivePoint(int x, int y) {
    super(0, 0);
    this.move(x, y);
  }

  /**
   * {@code setter}
   * Point 클래스의 {@code move} 메서드를 오버라이드함
   * 점을 특정 위치로 이동합니다.
   * 
   * @param {@code x} 점의 x좌표
   * @param {@code y} 점의 y좌표
   */
  @Override
  protected void move(int x, int y) {
    if (x < 0 || y < 0) return;
    super.move(x, y);
  }

  /**
   * 현재 표현하고 있는 점에 대한 정보를 문자열로 반환합니다.
   * @return {@code String} 점 정보
   */
  public String toString() {
    return String.format("(%d, %d)의 점", this.getX(), this.getY());
  }
}