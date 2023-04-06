import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt(), k = sc.nextInt();
    int ables = Math.min(n/2, m);
    int kPops = Math.max(n - ables*2, 0) + Math.max(m - ables, 0);
    while (k > kPops) {
      kPops += 3;
      ables -= 1;
    }
    System.out.println(ables);
  }
}