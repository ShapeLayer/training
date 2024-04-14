import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    // 문제 제시 코드
    Scanner scanner = new Scanner(System.in);
    System.out.print("수학, 과학, 영어순으로 3개의 점수 입력>>");
    int math = scanner.nextInt();
    int science = scanner.nextInt();
    int english = scanner.nextInt();
    Grade me = new Grade(math, science, english);
    System.out.println("평균은 " + me.average());
    // average()는 평균을 계산하여 리턴
    scanner.close();
  }
}

class Grade {
  int math;
  int science;
  int english;

  public Grade(int math, int science, int english) {
    this.math = math;
    this.science = science;
    this.english = english;
  }

  int average() {
    return (this.math + this.science + this.english) / 3;
  }
}