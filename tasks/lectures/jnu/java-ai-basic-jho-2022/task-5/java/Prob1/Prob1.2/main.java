package main;
import etc.Calc;

/**
 * MainApp 클래스
 * 
 * 일련의 자바 애플리케이션의 진입점입니다.
 */
public class MainApp {
  // 문제 제시 코드
  public static void main (String[] args) {
    Calc c = new Calc(10,20);
    System.out.println(c.sum());
  }
}