import java.util.Scanner;
import java.util.Arrays;

public class Main {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int[] dwarfs = new int[9];
    for (int i = 0; i < 9; i++) {
      dwarfs[i] = in.nextInt();
    }
    for (int i = 0; i < 9; i++) {
      for (int j = 0; j < 9; j++) {
        if (i == j) continue;
        int sums = Arrays.stream(dwarfs).sum();
        sums -= (dwarfs[i] + dwarfs[j]);
        if (sums == 100) {
          for (int k = 0; k < 9; k++) {
            if (k == i || k == j) continue;
            System.out.println(dwarfs[k]);
          }
          return;
        }
      }
    }
  }
}