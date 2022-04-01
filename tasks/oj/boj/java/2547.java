import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for (int i = 0; i < n; i++) {
      int loops = sc.nextInt();
      int candies = 0;
      for (int j = 0; j < loops; j++) {
        candies += sc.nextLong() % loops;
      }
      if (candies % loops == 0) System.out.println("YES");
      else System.out.println("NO");
    }
  }
}