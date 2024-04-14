import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    // 문제 제시 코드
    TV myTV = new TV("LG", 2017, 32);
    myTV.show();
  }
}

class TV {
  String name;
  int manufactures;
  int inch;

  public TV(String name, int manufactures, int inch) {
    this.name = name;
    this.manufactures = manufactures;
    this.inch = inch;
  }

  public void show() {
    System.out.println(String.format("%s에서 만든 %d년형 %d인치 TV", this.name, this.manufactures, this.inch));
  }
}