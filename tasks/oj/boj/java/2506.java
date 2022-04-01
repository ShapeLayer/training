import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int score = 0;
    int offset = 0;
    for (int i = 0; i < n; i++) {
      if (sc.nextInt() == 1) {
        score += offset + 1;
        offset += 1;
      } else {
        offset = 0;
      }
    }
    System.out.println(score);
  }
}