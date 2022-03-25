// 교재 9번 문제
import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    System.out.print("원의 중심과 반지름 입력 >> ");
    double cx = sc.nextDouble();
    double cy = sc.nextDouble();
    double radius = sc.nextDouble();
    System.out.print("점 입력 >> ");
    double x = sc.nextDouble();
    double y = sc.nextDouble();
    double dis = Math.sqrt(Math.pow(cx-x, 2) + Math.pow(cy-y, 2));
    if (dis <= radius)
      System.out.println(String.format("점 (%f, %f)는 원 안에 있다.", x, y));
    else
      System.out.println(String.format("점 (%f, %f)는 원 밖에 있다.", x, y));
  }
}