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

class Circle {
  int x, y, radius;

  Circle(int x, int y, int radius) {
    this.x = x;
    this.y = y;
    this.radius = radius;
  }

  public String toString() { return String.format("Circle(%d, %d)반지름%d", this.x, this.y, this.radius); }
  boolean equals(Circle circle) { return this.x == circle.x && this.y == circle.y; }
}
