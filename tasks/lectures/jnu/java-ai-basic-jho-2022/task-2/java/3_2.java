import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int gets = (int)2e9, min = gets; // gets를 입력, min을 최솟값으로 지정, INF로 초기화
    String[] arr = {"첫", "두", "세"}; // 문장 일부분을 배열로 초기화
    for (String var: arr) { // foreach 구문 사용, arr.length 만큼 반복
      System.out.print(var+"번째 정수를 입력하세요: "); // 문장 병합
      gets = sc.nextInt(); // 입력
      min = min < gets ? min : gets; // min값 갱신
    }
    System.out.println();
    System.out.println(String.format("Min값은 %d입니다.", min));
  }
}