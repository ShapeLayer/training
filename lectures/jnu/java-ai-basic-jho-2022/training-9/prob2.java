public class Main {
  public static void main(String [] args) {
    IPTV iptv = new IPTV("192.1.1.2", 32, 2048);
    iptv.printProperty();
  }
}

class TV {
  private int size;
  public TV (int size) { this.size = size; }
  protected int getSize() { return size; }
}

class ColorTV extends TV {
  private int size;
  private int colors;

  public ColorTV (int size, int colors) {
    super(size);
    this.colors = colors;
  }
  protected int getColors() { return this.colors; }

  public void printProperty() {
    System.out.println(String.format("%d인치 %d컬러", this.getSize(), this.getColors()));
  }
}

class IPTV extends ColorTV {
  private String ip;

  IPTV(String ip, int size, int colors) {
    super(size, colors);
    this.ip = ip;
  }

  protected String getIP() { return this.ip; }

  public void printProperty() {
    System.out.println("나의 IPTV는 "+this.getIP()+" 주소의 "+this.getSize()+"인치 "+this.getColors()+"컬러");
  }
}