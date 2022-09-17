import java.util.Scanner;
import java.util.Vector;

public class Main {
  public static void main(String[] args) {
    // 입력을 받기 위해 Scanner 객체 생성
    Scanner sc = new Scanner(System.in);

    // List<Integer> 벡터 객체 생성
    Vector<Integer> gets = new Vector<Integer>();

    // 입력 받을 변수 선언: nextInt()를 이 변수에 할당함
    int get = -1;

    System.out.print("정수(-1이 입력될 때까지) >> ");

    // 반복문 시작
    do {
      get = sc.nextInt();
      if (get == -1) continue; // 입력이 -1이라면 while()로 이동
      gets.add(get); // 입력이 -1이 아니라면 리스트에 추가
    } while (get != -1);
    // -1이라면 반복문 중지
    
    // 최대값 검색: 입력값은 모두 양의 정수이므로 음의 정수로 초기화 후 처리 시작
    int max = -1;
    for (int n: gets) // foreach문 사용
      if (max < n) max = n;

    System.out.println("가장 큰 수는 " + max);
  }
}