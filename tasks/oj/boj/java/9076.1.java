import java.util.Scanner;
import java.util.Arrays;

public class Main {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    for (int i = 0; i < n; i++) {
      int[] scores = new int[5];
      for (int j = 0; j < 5; j++) scores[j] = in.nextInt();
      int max = scores[0]; int min = scores[0]; int maxIdx = 0; int minIdx = 0;
      for (int j = 1; j < 5; j++) {
        if (max < scores[j]) {
          max = scores[j];
          maxIdx = j;
        }
        else if (min > scores[j]) {
          min = scores[j];
          minIdx = j;
        }
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
      max = middleScores[0]; min = middleScores[0];
      for (int j = 1; j < 3; j++) {
        if (max < middleScores[j]) max = middleScores[j];
        else if (min > middleScores[j]) min = middleScores[j];
      }
      if (max - min >= 4) {
        System.out.println("KIN");
      } else {
        System.out.println(Arrays.stream(middleScores).sum());
      }
    }
  }
}