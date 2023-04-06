import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    double[] prices = {350.34, 230.90, 190.55, 125.30, 180.90};
    int n = sc.nextInt();
    for (int i = 0; i < n; i++) {
      double sums = 0;
      for (int j = 0; j < 5; j++) {
        sums += prices[j] * sc.nextInt();
      }
      System.out.println(String.format("$%.2f", sums));
    }
  }
}