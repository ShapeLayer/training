import java.util.Scanner;
import java.lang.Math;

public class Main {
  public static void main(String args[]) {
    double distance = 40 * Math.pow(12, 23);
    double speed = 24 * 365;
    System.out.println("걸리는 시간은 약 " + distance/(600000*speed) + " 광년 입니다.");
  }
}