import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    // 값 초기화
    int gets = -1, arr[];
    System.out.print("정수 몇 개? >> ");
    gets = sc.nextInt();
    // 입력값만큼의 크기를 가진 배열 생성
    arr = new int[gets];
    
    // 초기화
    for (int i = 0; i < gets; i++) arr[i] = (int)(Math.random()*100+1);
    
    // 각 열에서 몇개 값을 출력했는지 기록함
    int lnCounts = 0;
    for (int i = 0; i < gets; i++) {
      System.out.print(String.format("%d ", arr[i]));
      lnCounts++;
      // 만약 깂을 10번 출력했다면 개행
      if (lnCounts % 10 == 0) System.out.println();
    }

    // 터미널 환경에서 프로세스를 실행하면
    // 종료 시 개행되어야 다음 터미널 명령을 깔끔하게 입력할 수 있음.
    System.out.println();
  }
}