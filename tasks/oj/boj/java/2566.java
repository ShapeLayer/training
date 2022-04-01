import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int max = -1, mx_row = -1, mx_col = -1;
    for (int row = 1; row < 10; row++) {
      for (int col = 1; col < 10; col++) {
        int gets = sc.nextInt();
        if (gets > max) {
          max = gets;
          mx_row = row;
          mx_col = col;
        }
      }
    }
    System.out.println(max);
    System.out.println(String.format("%d %d", mx_row, mx_col));
  }
}