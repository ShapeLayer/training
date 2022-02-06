import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    for (int i = 1; i < n+1; i++) {
      for (int j = 0; j < i; j++) { System.out.print("*"); }
      for (int j = 0; j < 2*(n-i); j++) { System.out.print(" "); }
      for (int j = 0; j < i; j++) { System.out.print("*"); }
      System.out.println();
    }
    for (int i = n-1; i > 0; i--) {
      for (int j = 0; j < i; j++) { System.out.print("*"); }
      for (int j = 0; j < 2*(n-i); j++) { System.out.print(" "); }
      for (int j = 0; j < i; j++) { System.out.print("*"); }
      System.out.println();
    }
  }
}