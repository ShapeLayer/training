public class Main {
  public static void main(String[] args) {
    // 문제 제시 값
    int n[][] = {{1},{1,2,3},{1},{1,2,3,4},{1,2}};

    // 배열을 행렬로 생각했을 때
    // 첫번째 for문으로 행 조회
    for (int i = 0; i < n.length; i++) {
      // 두번째 for문으로 열 조회
      for (int j = 0; j < n[i].length; j++) {
        // (i, j)번 요소 조회
        System.out.print(String.format("%d ", n[i][j]));
      }
      // 하나의 열을 모두 조회하면 개행
      System.out.println();
    }
  }
}