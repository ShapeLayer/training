import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class Main {
  public static void main(String[] args) {
    // 입력을 받아오기 위해 Scanner 객체 생성
    Scanner sc = new Scanner(System.in);

    // 리스트 객체 생성
    List<Character> grades = new ArrayList<Character>();

    System.out.print("6개의 학점을 빈 칸으로 분리 입력 (A/B/C/D/E/F) >> ");
    for (int i = 0; i < 6; i++)
      // sc.next()를 통한 입력은 한 문자(char형)만 받아오는 것이 아니기 때문에 String 형으로 반환함.
      // 따라서 charAt() 메서드를 사용하여 char 형 불러옴
      grades.add(sc.next().charAt(0));
    
    // 점수 합계용 변수 선언
    double sums = 0;
    for (char grade: grades) { // foreach문 사용
      // switch-case문으로 처리 시작
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
          // 학점 F가 존재한다는 맥락 차원에서 추가
          sums += 0;
          break;
      }
    }

    System.out.println(sums/6);
  }
}