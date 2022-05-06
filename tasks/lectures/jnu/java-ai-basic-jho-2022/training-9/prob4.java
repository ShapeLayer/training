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

class Point {
  private int x, y;
  public Point(int x, int y) { this.x = x; this.y = y; }
  public int getX() { return x; }
  public int getY() { return y; }
  protected void move(int x, int y) { this.x = x; this.y = y; }
}

class Point3D extends Point {
  private int z;
  public Point3D(int x, int y, int z) {
    super(x, y);
    this.z = z;
  }
  public void move(int x, int y, int z) { super.move(x, y); setZ(z); }
  public void moveUp() { this.setZ(this.getZ()+1); }
  public void moveDown() { this.setZ(this.getZ()-1); }
  public int getZ() { return this.z; }
  public void setZ(int z) { this.z = z; }
  public String toString() { return String.format("(%d, %d, %d)의 점", this.getX(), this.getY(), this.getZ()); }
}
