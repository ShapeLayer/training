public class Main {
  public static void main(String[] args) {
    System.out.println("Start declaring ProxyImage instances.");
    Image image1 = new ProxyImage("puts1.in");
    Image image2 = new ProxyImage("puts2.in");

    System.out.println("Start displaying all images.");
    image1.DisplayImage();
    image2.DisplayImage();
  }
}

public interface Image {
  public void DisplayImage();
}

public class RealImage implements Image {
  private String fileName;

  public RealImage(String fileName) {
    this.fileName = fileName;
    this.LoadImage();
  }

  private void LoadImage() {
    System.out.println("Real Image Loaded: " + this.fileName);
  }
  
  @Override
  public void DisplayImage() {
    System.out.println("Real Image Displayed: " + this.fileName);
  }
}

public class ProxyImage implements Image {
  private String fileName;
  private RealImage realImage;

  public ProxyImage(String fileName) {
    this.fileName = fileName;
    System.out.println("Proxy Image Constructed: " + this.fileName);
  }

  @Override
  public void DisplayImage() {
    if (realImage == null) {
      realImage = new RealImage(this.fileName);
    }
    realImage.DisplayImage();
  }
}
