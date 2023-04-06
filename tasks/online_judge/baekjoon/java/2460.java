import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int people = 0, max = 0;
    for (int i = 0; i < 10; i++) {
      int out = sc.nextInt(), in = sc.nextInt();
      people += (in - out);
      if (max < people) max = people;
    }
    System.out.println(max);
  }
}