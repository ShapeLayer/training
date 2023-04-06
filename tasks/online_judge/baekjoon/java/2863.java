import java.util.Scanner;
import java.util.Arrays;

public class Main {
  public static void main (String[] args) {
    Scanner sc = new Scanner(System.in);
    double a = sc.nextDouble(), b = sc.nextDouble(), c = sc.nextDouble(), d = sc.nextDouble();
    double[] gets = {a/c+b/d, c/d+a/b, d/b+c/a, b/a+d/c};
    double max = Arrays.stream(gets).max().getAsDouble();
    for (int i = 0; i < 4; i++)
      if (gets[i] == max)
        System.out.println(i);
  }
}