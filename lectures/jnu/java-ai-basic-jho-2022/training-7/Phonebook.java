import java.util.Scanner;

public class Phonebook {
  public static void main(String[] args) {
    Phone p = new Phone("a", "B");
    Scanner sc = new Scanner(System.in);
    System.out.print("인원수 >> ");
    int n = sc.nextInt();
    Phone[] phones = new Phone[n];
    for (int i = 0; i < n; i++) {
      System.out.print("이름과 전화번호 (이름과 번호는 빈 칸없이 입력 >>> ");
      String name = sc.next();
      String tel = sc.next();
      phones[i] = new Phone(name, tel);
    }
    System.out.println("저장되었습니다…");
    while (true) {
      System.out.print("검색할 이름 >> ");
      String gets = sc.next();
      boolean flag = false;
      if (gets.equals("그만")) break;
      for (int i = 0; i < n; i++) {
        if (phones[i].getName().equals(gets)) {
          flag = true;
          System.out.println(String.format("%s의 번호는 %s입니다.", phones[i].getName(), phones[i].getTel()));
        }
      }
      if (!flag) { System.out.println(String.format("%s 이(가) 없습니다.", gets)); }
    }
    System.out.println("프로그램을 종료합니다.");
  }
}

class Phone {
  private String name;
  private String tel;

  public Phone(String name, String tel) {
    this.name = name; this.tel = tel;
  }
  
  public String getName() { return name; }
  public String getTel() { return tel; }
}
