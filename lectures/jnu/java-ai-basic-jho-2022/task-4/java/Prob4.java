/**
 * @author @ShapeLayer
 */

// 문제 제시 코드
public class Main {
  public static void main(String [] args) {
    Shape donut = new Circle(10); // 반지름이 10인 원 객체
    donut.redraw();
    System.out.println("면적은 " + donut.getArea());
  }
}

// 문제 제시 인터페이스
interface Shape {
  final double PI = 3.14; // 상수
  void draw(); // 도형을 그리는 추상 메소드
  double getArea(); // 도형의 면적을 리턴하는 추상 메소드
  default public void redraw() { // 디폴트 메소드
    System.out.print("--- 다시 그립니다. ");
    draw();
  }
}

/**
 * Circle 클래스
 * {@code Shape} 인터페이스를 구현함
 * 
 * Circle 클래스는 원을 그리고 처리하는데 유용한 메서드가 포함되어있습니다.
 */
class Circle implements Shape {
  /**
   * 원의 면적
   */
  double area;
  /**
   * 원의 반지름
   */
  double radius;

  /**
   * Circle 객체를 생성합니다.
   * @param radius {@code int} 원의 반지름
   */
  Circle(int radius) {
    this.radius = radius;
    this.area = this.radius * this.radius * this.PI;
  }

  /**
   * 원을 그리고 결과를 출력합니다.
   */
  @Override public void draw() {
    System.out.println("반지름이 " + this.radius + "인 원입니다.");
  }

  /**
   * 원의 면적을 반환합니다.
   * @return {@code double} 원의 면적
   */
  @Override public double getArea() { return this.area; }
}