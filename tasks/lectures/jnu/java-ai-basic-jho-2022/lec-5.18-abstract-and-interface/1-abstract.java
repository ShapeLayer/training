public class Main {
  // 추상 메서드 (Abstract Method): 선언만 하고 구현하지 않은 메서드, abstract 키워드 사용
  // public abstract String getName();
  // public abstract void setName(String s);
  public static void main(String[] args) {
    Line line = new Line();
    line.draw();

    Rect rect = new Rect();
    rect.draw();
  }
}

public abstract class Shape {
  public Shape() {}
  public void paint() { draw(); }
  abstract public void draw();
}

class Line extends Shape {
  @Override
  public void draw() {
    System.out.println("Line");
  }
}

class Rect extends Shape {
  // @Override 어노테이션이 존재하는 이유
  // 오버라이드가 제대로 진행될 수 있는지 컴파일러가 확인을 거쳐줌
  // 따라서 오버라이드 어노테이션을 사용하는 것이 좋은 코딩 습관
  public void draw() {
    System.out.println("Rect");
  }
}