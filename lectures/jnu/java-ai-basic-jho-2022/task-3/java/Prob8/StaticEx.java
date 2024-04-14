/**
 * @author @ShapeLayer
 */

// 코드 Javadoc 문서화
// 참조: https://docs.oracle.com/en/java/javase/17/docs/specs/javadoc/doc-comment-spec.html

import java.util.Arrays;

public class StaticEx {
  public static void main(String[] args) {
    // 문제 제시 코드
    int[] array1 = { 1, 5, 7, 9 };
    int[] array2 = { 3, 6, -1, 100, 77 };
    int[] array3 = ArrayUtil.concat(array1, array2);
    ArrayUtil.print(array3);
  }
}

/**
 * ArrayUtil 클래스
 * 
 * ArrayUtil 클래스는 배열을 좀 더 쉽게 제어할 수 있는 메서드를 포함하고 있습니다.
 */
class ArrayUtil {
  /**
   * 두 정수 배열을 하나로 병합합니다.
   * @param a {@code int[]} 첫 번째 정수 배열
   * @param b {@code int[]} 두 번째 정수 배열
   * @return {@code int[]} 배열 병합 결과
   */
  public static int[] concat(int[] a, int[] b) {
    // 배열 a와 b를 연결한 새로운 배열 리턴
    int[] newArr = new int[a.length + b.length];
    System.arraycopy(a, 0, newArr, 0, a.length);
    System.arraycopy(b, 0, newArr, a.length, b.length);
    
    /* 시간복잡도 O(n)인 처리 방법
    for (int i = 0; i < a.length; i++) newArr[i] = a[i];
    for (int i = 0; i < b.length; i++) newArr[a.length + i] = b[i];
    */
    return newArr;
  }

  /**
   * 정수 배열을 출력합니다.
   * 
   * @param a {@code int[]} 정수 배열
   */
  public static void print(int[] a) {
    // 배열 a를 출력
    // System.out.println(Arrays.toString(a));

    // print()는 출력 후 개행하지 않으므로 한 줄을 여러 줄에 걸쳐서 출력
    System.out.print("[ ");
    for (int i = 0; i < a.length; i++) 
      System.out.print(a[i] + " ");
    System.out.println("]");
  }
}