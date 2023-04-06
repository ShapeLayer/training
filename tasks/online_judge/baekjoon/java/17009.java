import java.util.Scanner;

public class Main {
  // https://stackoverflow.com/questions/19766566/java-multiple-scanners/19766633#19766633
  static final Scanner in = new Scanner(System.in);
  public static void main(String args[]) {
    int score[] = {0, 0};
    for (int i = 0; i < 2; i++) {
      for (int j = 3; j > 0; j--) {
        score[i] += in.nextInt() * j;
      }
    }
    System.out.println(score[0] == score[1] ? "T" : (score[0] > score[1] ? "A" : "B"));
  }
}