import java.util.Scanner;

public class Main {
  public static boolean isComplete(String word) {
    char lastWord = word.charAt(word.length() - 1);
    if (lastWord < 0xAC00 || lastWord > 0xD7A3) { return false; }
    return (lastWord - 0xAC00) % 28 > 0;
  }

  public static void main(String[] args) {
    System.out.println("한영 단어 검색 프로그램입니다.");
    Scanner sc = new Scanner(System.in);
    while (true) {
      System.out.print("한글 단어? ");
      String gets = sc.next();
      if (gets.equals("종료")) {
        break;
      }
      String res = Dictionary.kor2Eng(gets);
      System.out.println(String.format("%s%s %s",
        gets,
        Main.isComplete(gets) ? "은" : "는",
        res != null ? res : "저의 사전에 없습니다."
      ));
    }
    System.out.println("프로그램을 종료합니다.");
  }
}

class Dictionary {
  private static String[] kor = {"사랑", "아기", "돈", "미래", "희망"};
  private static String[] eng = {"love", "baby", "money", "future", "hope"};
  public static String kor2Eng(String word) {
    for (int i = 0; i < kor.length; i++) {
      if (kor[i].equals(word)) {
        return eng[i];
      }
    }
    return null;
  }
}