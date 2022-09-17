/**
 * @author @ShapeLayer
 */

// 문제 제시 코드
public class Main {
  public static void main(String[] args){
    Circle a = new Circle(2, 3, 5);
    Circle b = new Circle(2, 3, 30);
    System.out.println("원 a : " + a);
    System.out.println("원 b : " + b);
    if(a.equals(b))
      System.out.println("같은 원");
    else
      System.out.println("서로 다른 원");
  }
}

/**
 * Circle 클래스
 * 
 * Circle 클래스는 2차원 상의 원의 데이터를 처리할 수 있도록 작성되었습니다.
 */
class Circle {
  /**
   * 원 중심의 x좌표
   */
  int x;

  /**
   * 원 중심의 y좌표
   */
  int y;

  /**
   * 원의 반지름
   */
  int radius;

  /**
   * Circle 객체를 생성합니다.
   * @param x {@code int} 원 중심의 x좌표
   * @param y {@code int} 원 중심의 y좌표
   * @param radius {@code int} 원의 반지름
   */
  Circle(int x, int y, int radius) {
    this.x = x;
    this.y = y;
    this.radius = radius;
  }

  /**
   * Circle 객체 정보를 요약하여 반환합니다.
   * @return {@code String} 요약 정보
   */
  public String toString() { return String.format("Circle(%d, %d)반지름%d", this.x, this.y, this.radius); }

  /**
   * 두 원이 동일한지 확인합니다.
   * @return {@code boolean} 동일 여부
   */
  boolean equals(Circle circle) { return this.x == circle.x && this.y == circle.y; }
}
