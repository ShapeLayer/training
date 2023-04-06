import java.util.Scanner;
import java.util.Arrays;

public class Main {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    for (int i = 0; i < n; i++) {
      int[] scores = new int[5];
      for (int j = 0; j < 5; j++) scores[j] = in.nextInt();
      int max = Arrays.stream(scores).max().orElse(0);
      int min = Arrays.stream(scores).min().orElse(0);
      int maxIdx = 0; int minIdx = 0;
      for (int j = 0; j < 5; j++) {
        if (scores[j] == max) maxIdx = j;
        else if (scores[j] == min) minIdx = j;
      }
      int[] middleScores = new int[3];
      int pointer = 0;
      boolean maxFlag = false; boolean minFlag = false;
      for (int j = 0; j < 5; j++) {
        if (scores[j] == max && !maxFlag) {
          maxFlag = true;
        } else if (scores[j] == min && !minFlag) {
          minFlag = true;
        } else {
          middleScores[pointer] = scores[j];
          pointer++;
        }
      }
      if (Arrays.stream(middleScores).max().orElse(0) - Arrays.stream(middleScores).min().orElse(0) >= 4) {
        System.out.println("KIN");
      } else {
        System.out.println(Arrays.stream(middleScores).sum());
      }
    }
  }
}