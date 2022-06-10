public class Main {
  public static void main(String[] args) {
    impls impl = new impls();
    System.out.println(impl.get());
  }
}

interface example {
  int TIMEOUT = 10000;
}

public class impls implements example {
  public int get() {
    return this.TIMEOUT;
  }
}
