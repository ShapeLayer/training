public class Main {
  public static void main(String [] args) {
    ColorTV myTV = new ColorTV(32, 1024);
    myTV.printProperty();
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
  protected int getColors() {
    return this.colors;
  }
  public void printProperty() {
    System.out.println(String.format("%d인치 %d컬러", this.getSize(), this.getColors()));
  }
}
