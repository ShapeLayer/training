import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    double distance = 40 * Math.pow(10, 12);
    double speed = 3600 * 24 * 365;
    System.out.println("걸리는 시간은 약 " + distance/(300000*speed) + " 광년 입니다.");
  }
}