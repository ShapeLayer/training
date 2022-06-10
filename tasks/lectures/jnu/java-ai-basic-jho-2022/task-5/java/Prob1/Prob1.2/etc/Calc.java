package etc;

// class Calc {
// main.java:2: error: Calc is not public in etc; cannot be accessed from outside package
/**
 * Calc 클래스
 *
 * 간단한 수 계산에 대한 메서드를 포함하고 있습니다.
 */
public class Calc {
  // 문제 제시 코드
  private int x,y;
  public Calc(int x, int y) {this.x = x ; this.y = y; }
  public int sum() { return x+y; }
}