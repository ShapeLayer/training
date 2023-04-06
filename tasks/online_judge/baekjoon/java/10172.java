/*
  JEP 378: Text Blocks covers this functionality and is included in JDK 15.
  https://stackoverflow.com/questions/878573/does-java-have-support-for-multiline-strings/50155171#50155171
*/
public class Main {
  public static void main(String args[]) {
    System.out.println("""
    |\\_/|
    |q p|   /}
    ( 0 )\"\"\"\\
    |\"^\"`    |
    ||_/=\\\\__|
    """);
  }
}