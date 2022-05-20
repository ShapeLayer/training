/**
 * @author @ShapeLayer
 */

// 문제 제시 코드
public class Main {
  static public void main(String [] args) {
    Shape [] list = new Shape[3]; // Shape을 상속받은 클래스 객체의 래퍼런스 배열
    list[0] = new Circle(10); // 반지름이 10인 원 객체
    list[1] = new Oval(20, 30); // 20x30 사각형에 내접하는 타원
    list[2] = new Rect(10, 40); // 10x40 크기의 사각형
    for(int i=0; i<list.length; i++) list[i].redraw();
    for(int i=0; i<list.length; i++) System.out.println("면적은 " + list[i].getArea());
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

/**
 * Oval 클래스
 * {@code Shape} 인터페이스를 구현함
 * 
 * Oval 클래스는 타원을 그리고 처리하는데 유용한 메서드가 포함되어 있습니다.
 */
class Oval implements Shape {
  /**
   * 타원의 면적
   */
  double area;
  /**
   * 타원의 가로 축
   */
  double width;
  /**
   * 타원의 세로 축
   */
  double height;

  /**
   * Oval 객체를 생성합니다.
   * @param width {@code int} 타원의 가로 축
   * @param height {@code int} 타원의 세로 축
   */
  Oval(int width, int height) {
    this.width = width;
    this.height = height;
    // 타원 면적 공식: PI*a*b
    this.area = this.PI * this.width * this.height;
  }
  
  /**
   * 타원을 그리고 결과를 출력합니다.
   */
  @Override public void draw() {
    System.out.println(String.format("%dx%d에 내접하는 타원입니다.", (int)width, (int)height));
  }
  /**
   * 타원의 면적을 반환합니다.
   * @return {@code double} 타원의 면적
   */
  @Override public double getArea() { return this.area; }
}

/**
 * Rect 클래스
 * {@code Shape} 인터페이스를 구현함
 * 
 * Rect 클래스는 직사각형을 그리고 처리하는데 유용한 메서드가 포함되어 있습니다.
 */
class Rect implements Shape {
  /**
   * 직사각형의 면적
   */
  double area;
  /**
   * 직사각형의 가로 길이
   */
  double width;
  /**
   * 직사각형의 세로 길이
   */
  double height;

  /**
   * Rect 객체를 생성합니다.
   * @param width {@code int} 직사각형의 가로 길이
   * @param height {@code int} 직사각형의 세로 길이
   */
  Rect(int width, int height) {
    this.width = width;
    this.height = height;
    // 면적 공식: a*b
    this.area = this.width * this.height;
  }

  /**
   * 직사각형을 그리고 결과를 출력합니다.
   */
  @Override public void draw() {
    System.out.println(String.format("%dx%d크기의 사각형 입니다.", (int)width, (int)height));
  }
  /**
   * 직사각형의 면적을 반환합니다.
   * @return {@code double} 직사각형의 면적
   */
  @Override public double getArea() { return this.area; }
}
