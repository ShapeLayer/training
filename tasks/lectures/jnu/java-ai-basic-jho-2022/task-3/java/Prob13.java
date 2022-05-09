/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

public class Main {
  public static void main(String[] args) {
    Point3D p = new Point3D(1,2,3); // 1,2,3은 각각 x, y, z 축의 값.
    System.out.println(p.toString() + "입니다.");
    p.moveUp(); // z축 1값 증가
    System.out.println(p.toString() + "입니다.");
    p.moveDown(); // z축 1값 감소
    p.move(10, 10); // x, y 축의 해당 위치로 이동
    System.out.println(p.toString() + "입니다.");
    p.move(100, 200, 300); // x, y, z 축의 해당 위치로 이동
    System.out.println(p.toString() + "입니다.");
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
   * @param x {@code 새 x좌표}
   * @param y {@code 새 y좌표}
   */
  protected void move(int x, int y) { this.x = x; this.y = y; }
}

/**
 * Point3D 클래스
 * 
 * Point 클래스를 상속함
 * Point3D 클래스는 3차원 상의 한 점을 표현하는데 활용되는 클래스입니다.
 */
class Point3D extends Point {
  /**
   * 점의 z 좌표입니다.
   */
  private int z;

  /**
   * Point3D 객체를 생성합니다.
   * @param x x좌표
   * @param y y좌표
   * @param z z좌표
   */
  public Point3D(int x, int y, int z) {
    // 부모의 생성자 호출
    super(x, y);
    this.z = z;
  }
  
  /**
   * 점의 x좌표, y좌표, z좌표를 이동시킵니다. (= setter)
   * @param x 새 x좌표
   * @param y 새 y좌표
   * @param z 새 z좌표
   */
  public void move(int x, int y, int z) { super.move(x, y); setZ(z); }

  /**
   * z좌표값을 1 증가시킵니다.
   */
  public void moveUp() { this.setZ(this.getZ()+1); }
  /**
   * z좌표값을 1 감소시킵니다.
   */
  public void moveDown() { this.setZ(this.getZ()-1); }
  /**
   * z좌표를 반환합니다.
   * @return {@code int} 점의 z좌표
   */
  public int getZ() { return this.z; }
  /**
   * {@code setter} z좌표를 설정합니다.
   * @param z {@code int} 새 z좌표
   */
  public void setZ(int z) { this.z = z; }

  /**
   * 객체의 정보를 String형으로 변환해 반환합니다.
   * @return {@code String} 객체의 정보
   */
  public String toString() { return String.format("(%d, %d, %d)의 점", this.getX(), this.getY(), this.getZ()); }
}
