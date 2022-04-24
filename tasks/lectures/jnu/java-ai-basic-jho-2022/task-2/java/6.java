import java.lang.Math;

public class Main {
  public static void main(String[] args) {
    // 배열 초기화
    int[][] arr = new int[4][4];
    // 이중 포문으로 배열의 각 값 접근
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        arr[i][j] = (int)(Math.random()*10+1); // 문제 제시 값
      }
    }
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        // 행 출력
        System.out.print(String.format("%d ", arr[i][j]));
      }
      // 하나의 열을 모두 출력하면 개행
      System.out.println();
    }
  }
}