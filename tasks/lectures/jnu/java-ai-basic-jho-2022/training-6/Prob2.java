import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String course[] = {"java", "c++", "HTML5", "컴퓨터구조", "안드로이드"};
    int score[] = {95, 88, 76, 62, 55};
    String name;
    while(true) {
      System.out.print("과목 이름 >> ");
      name = sc.next();
      if (name.equals("그만")) { break; }
      boolean flag = false;
      for (int i = 0; i < course.length; i++) {
        if (course[i].toLowerCase().equals(name.toLowerCase())) {
          System.out.println(String.format("%s의 점수는 %d", name, score[i]));
          flag = true;
        }
      }
      if (!flag) System.out.println("없는 과목입니다.");
    }
  }
}