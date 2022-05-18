public class Main {
  public static void main(String[] main) {
    IPhone IPhoneVar; // 변수 선언 가능
    // new IPhone() // 객체 생성 불가능
    IPhoneVar = new Galaxy();
    IPhoneVar.printLogo();
  }
}

interface IPhone {
  public static final int TIMEOUT = 10000;
  public abstract void sendCall();
  public abstract void receiveCall();
  public default void printLogo() {
    System.out.println("** Phone **");
  }
}

interface Samsung {
  public abstract void enableGOS();
}

class Galaxy implements IPhone, Samsung { // 다중 상속 가능
  @Override
  public void sendCall() {}
  @Override
  public void receiveCall() {}
  @Override
  public void enableGOS() {}
}