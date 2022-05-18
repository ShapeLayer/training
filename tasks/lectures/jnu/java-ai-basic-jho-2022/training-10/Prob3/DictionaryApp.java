public class DictionaryApp {
  public static void main(String[] args) {
    Dictionary dic = new Dictionary(10);
    dic.put("황기태", "자바");
    dic.put("이재문", "파이선");
    dic.put("이재문", "C++");
    System.out.println("이재문의 값은 " + dic.get("이재문"));
    System.out.println("황기태의 값은 " + dic.get("황기태"));
    dic.delete("황기태");
    System.out.println("황기태의 값은 " + dic.get("황기태"));
  }
}

abstract class PairMap {
  protected String keyArray [];
  protected String valueArray [];
  abstract String get(String key);
  abstract void put(String key, String value);
  abstract String delete(String key);
  abstract int length();
}

class Dictionary extends PairMap {
  int size;
  boolean availables[];
  public Dictionary(int size) {
    this.size = size;
    this.keyArray = new String[size];
    this.valueArray = new String[size];
    this.availables = new boolean[size];
  }

  @Override
  String get(String key) {
    for (int i = 0; i < this.size; i++) {
      if (!this.availables[i]) continue;
      if (key.equals(this.keyArray[i])) {
        return this.valueArray[i];
      }
    }
    return null;
  }

  @Override
  void put(String key, String value) {
    if (this.get(key) == null) {
      for (int i = 0; i < this.size; i++) {
        if (!this.availables[i]) {
          this.availables[i] = true;
          this.keyArray[i] = key;
          this.valueArray[i] = value;
          return;
        }
      }
      // abort error: no more spaces
      System.out.println("Error: No more spaces");
    } else {
      for (int i = 0; i < this.size; i++) {
        if (!this.availables[i]) continue;
        if (key.equals(this.keyArray[i])) {
          this.valueArray[i] = value;
          return;
        }
      }
    }
  }

  @Override
  String delete(String key) {
    for (int i = 0; i < this.size; i++) {
      if (!this.availables[i]) continue;
      if (key.equals(this.keyArray[i])) {
        // 실제로 삭제하지는 않음. 해당 공간이 비어있다고 표기한 후 나중에 덮어쓰기함.
        this.availables[i] = false;
        return this.valueArray[i];
      }
    }
    return null;
  }

  @Override
  int length() {
    int ables = 0;
    for (int i = 0; i < this.size; i++) {
      if (this.availables[i]) ables++;
    }
    return ables;
  }
}