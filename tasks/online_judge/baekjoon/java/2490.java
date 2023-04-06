import java.util.Scanner;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    for (int i = 0; i < 3; i++) {
      int front = 0, back = 0;
      for (int j = 0; j < 4; j++) {
        int gets = sc.nextInt();
        if (gets == 0) front++;
        else back++;
      }
      if (front == 1) System.out.println("A");
      else if (front == 2) System.out.println("B");
      else if (front == 3) System.out.println("C");
      else if (front == 4) System.out.println("D");
      else System.out.println("E");
    }
  }
}