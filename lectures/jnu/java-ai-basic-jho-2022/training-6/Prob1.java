// java Prob1.java 1 2 3 5 7 8 1 2 3 4

import java.util.Arrays;

public class Main {
  public static void main(String[] args) {
    int sums = 0;
    for (int i = 0; i < args.length; i++) {
      sums += Integer.parseInt(args[i]);
    }
    System.out.println("입력받은 인자 값의 평균은 : " + sums/(float)args.length);
  }
}