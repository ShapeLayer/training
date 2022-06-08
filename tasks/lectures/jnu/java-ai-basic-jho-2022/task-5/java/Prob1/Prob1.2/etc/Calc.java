package etc;

// class Calc {
// main.java:2: error: Calc is not public in etc; cannot be accessed from outside package
public class Calc {
 private int x,y;
 public Calc(int x, int y) {this.x = x ; this.y = y; }
 public int sum() { return x+y; }
}