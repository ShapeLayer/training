public class Main {
  public static void main(String[] args) {
    ColorPoint zeroPoint = new ColorPoint(); // (0,0) 위치의 BLACK 색점
    System.out.println(zeroPoint.toString() + "입니다.");
    ColorPoint cp = new ColorPoint(10, 10); // (10,10) 위치의 BLACK 색점
    cp.setXY(5, 5);
    cp.setColor("RED");
    System.out.println(cp.toString() + "입니다.");
  }
}

class Point {
  private int x, y;
  public Point(int x, int y) { this.x = x; this.y = y; }
  public int getX() { return x; }
  public int getY() { return y; }
  protected void move(int x, int y) { this.x = x; this.y = y; }
}

class ColorPoint extends Point {
  private String color = "BLACK";
  public ColorPoint() { this(0, 0); }
  public ColorPoint(int x, int y) { super(x, y); }
  public void setXY(int x, int y) { this.move(x, y); }
  public void setColor(String color) { this.color = color; }
  public String toString() { return String.format("%s색의 (%d, %d)의 점", this.color, this.getX(), this.getY()); }
}