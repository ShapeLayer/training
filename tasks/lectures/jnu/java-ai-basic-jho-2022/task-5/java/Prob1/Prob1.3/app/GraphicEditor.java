package app;
import base.Shape;
import derived.Circle;

/**
 * GraphicEditor 클래스
 *
 * GraphicEditor 클래스는 일련의 애플리케이션의 진입점을 포함하고 있습니다.
 */
public class GraphicEditor {
  // 문제 제시 코드
  public static void main(String[] args) {
    Shape shape = new Circle();
    shape.draw();
  }
}