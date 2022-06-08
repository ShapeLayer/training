import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    List<Character> grades = new ArrayList<Character>();

    System.out.print("6개의 학점을 빈 칸으로 분리 입력 (A/B/C/D/E/F) >> ");
    for (int i = 0; i < 6; i++)
      grades.add(sc.next().charAt(0));
    
    double sums = 0;
    for (char grade: grades) {
      switch (grade) {
        case 'A':
          sums += 4;
          break;
        case 'B':
          sums += 3;
          break;
        case 'C':
          sums += 2;
          break;
        case 'D':
          sums += 1;
          break;
        case 'F':
          // 학점 F가 존재한다는 Context 차원에서 추가
          sums += 0;
          break;
      }
    }

    System.out.println(sums/6);
  }
}