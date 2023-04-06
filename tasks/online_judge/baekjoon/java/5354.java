import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    for (int i = 0; i < n; i++) {
      int size = sc.nextInt();
      String puts = "";
      for (int j = 0; j < size; j++) {
        if (j == 0 || j == size-1)
          puts += "#".repeat(size) + "\n";
        else
          puts += "#" + "J".repeat(size-2) + "#\n";
      }
      System.out.println(puts);
    }
  }
}