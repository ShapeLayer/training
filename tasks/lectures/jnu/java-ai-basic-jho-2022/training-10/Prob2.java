import java.util.Collections;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n;
    String gets;
    StringStack stack;
    Scanner sc = new Scanner(System.in);
    System.out.print("총 스택 저장 공간의 크기 입력 >> ");
    n = sc.nextInt();
    stack = new StringStack(n);

    int i = 0;
    while (true) {
      System.out.print("문자열 입력 >> ");
      gets = sc.next();
      if (gets.equals("그만")) break;
      if (!stack.push(gets)) {
        System.out.println("스택이 꽉 차서 푸시 불가!");
      }
    }
    System.out.println("스택에 저장된 모든 문자열 팝 : " + String.join(" ", stack.getData()));
  }
}

interface Stack {
  int length();
  int capacity();
  String pop();
  boolean push(String val);
}

class StringStack implements Stack {
  int size, peek = -1;
  String data[];

  public StringStack(int size) {
    this.size = size;
    this.data = new String[this.size];
  }

  @Override
  public int length() { return this.size; }

  @Override
  public int capacity() { return peek+1; }

  @Override
  public boolean push(String val) {
    if (this.peek < this.length()-1) {
      this.peek++;
      this.data[this.peek] = val;
      return true;
    } else {
      return false;
    }
  }

  @Override
  public String pop() {
    if (this.peek < 0) return null;
    this.peek--;
    return this.data[this.peek+1];
  }

  public String[] getData() {
    String[] results = new String[this.length()];
    for (int i = 0; i < this.length(); i++) {
      results[i] = this.data[this.length()-1-i];
    }
    return results;
  }
}