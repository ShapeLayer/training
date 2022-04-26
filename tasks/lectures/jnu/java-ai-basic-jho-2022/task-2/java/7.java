import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    // 값 초기화
    int gets = -1, arr[];
    /*
     puts는 값이 이미 생성되었는지 확인하는 용도로 사용됨
     puts[val] = true라면 val은 이미 출력 대상인 것
     boolean[]은 디폴트 초기화값이 false임
     참조: https://www.tutorialspoint.com/how-can-we-initialize-a-boolean-array-in-java
    */
    boolean puts[] = new boolean[101];
    puts[0] = true; // 출력 범위가 1부터 100 사이 정수이므로 0은 사용되는 값이 아님: 다른 용도로 사용
    System.out.print("정수 몇 개? >> ");
    gets = sc.nextInt();
    // 입력값만큼의 크기를 가진 배열 생성
    arr = new int[gets];
    
    // 초기화
    for (int i = 0; i < gets; i++) {
      int val = 0; // 윗줄의 puts[0] = true;를 활용하기 위해 val을 0으로 초기화
      /*
       puts[0] = true이므로 while문 진입 가능.
       이후 랜덤값으로 갱신되었을 때
       * puts[val]이 false라면 사용되지 않은 값임을 의미하므로
         while문이 종료되고 그대로 값을 사용함
       * puts[val]이 true라면 이미 사용된 값이므로
         while문은 종료되지 않고 난수 생성을 재시도함.
      */
      while (puts[val]) { val = (int)(Math.random()*100+1); }
      puts[val] = true;
      arr[i] = val;
    }
    
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