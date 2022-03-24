import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt(), b = sc.nextInt(), c = sc.nextInt();
    System.out.println("x1 = " + (-b+Math.sqrt(Math.pow(b, 2)-4*a*c))/2*a);
    System.out.println("x2 = " + (-b-Math.sqrt(Math.pow(b, 2)-4*a*c))/2*a);
  }
}