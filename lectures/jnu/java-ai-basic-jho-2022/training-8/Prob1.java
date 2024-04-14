import java.util.Arrays;

public class Main {
  public static void main(String[] args) {
    int[] array1 = { 1, 5, 7, 9 };
    int[] array2 = { 3, 6, -1, 100, 77 };
    int[] array3 = ArrayUtil.concat(array1, array2);
    ArrayUtil.print(array3);
  }
}

class ArrayUtil {
  public static int[] concat(int[] a, int[] b) {
    // 배열 a와 b를 연결한 새로운 배열 리턴
    int[] newArr = new int[a.length + b.length];
    System.arraycopy(a, 0, newArr, 0, a.length);
    System.arraycopy(b, 0, newArr, a.length, b.length);
    return newArr;
  }
  public static void print(int[] a) {
    // 배열 a를 출력
    // System.out.println(Arrays.toString(a));
    System.out.print("[ ");
    for (int i = 0; i < a.length; i++) 
      System.out.print(a[i] + " ");
    System.out.println("]");
  }
}