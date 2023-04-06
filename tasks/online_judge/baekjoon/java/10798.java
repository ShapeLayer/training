import java.util.Scanner;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Main {
  public static void main(String args[]) {
    Scanner in = new Scanner(System.in);
    /*
      .\Main.java:8: error: generic array creation
      Queue<String>[] queue = new LinkedList<String>[5];
    */
    /*
      .\Main.java:17: warning: [unchecked] unchecked call to add(E) as a member of the raw type Queue
        queue[i].add(word);
                    ^
        where E is a type-variable:
         E extends Object declared in interface Queue
      1 warning
    */
    ArrayList<Queue<String>> queue = new ArrayList<Queue<String>>();
    int maxLength = 0;
    for (int i = 0; i < 5; i++) {
      queue.add(new LinkedList<String>());
      String puts = in.next();
      if (maxLength < puts.length()) {
        maxLength = puts.length();
      }
      for (String word : puts.split("")) {
        queue.get(i).add(word);
      }
    }
    for (int i = 0; i < maxLength; i++) {
      for (int j = 0; j < 5; j++) {
        String word = (String) queue.get(j).poll();
        System.out.print(word != null && !word.isEmpty() ? word : "");
      }
    }
  }
}