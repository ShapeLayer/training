import java.util.Scanner;
import java.util.Vector;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    Vector<Integer> gets = new Vector<Integer>();
    int get = -1;

    System.out.print("정수(-1이 입력될 때까지) >> ");

    do {
      get = sc.nextInt();
      if (get == -1) continue;
      gets.add(get);
    } while (get != -1);
    
    int max = -1;
    for (int n: gets)
      if (max < n) max = n;

    System.out.println("가장 큰 수는 " + max);
  }
}