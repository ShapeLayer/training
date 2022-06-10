public class Main {
  public static void main(String[] args) {
    Entity cat = new Mob("minecraft:cat", 20);
    Entity item = cat;
    //System.out.println(cat.health + " " + item.health);
    Mob zombie = new Mob("minecraft:zombie", 20);
    Entity skeleton = zombie;
    System.out.println(zombie.health/* + " " + skeleton.health*/);
  }
}

public class Entity {
  public String type;
  public Entity (String type) {
    this.type = type;
  }
}

public class Mob extends Entity {
  public int health;
  public Mob (String type, int health) {
    super(type);
    this.health = health;
  }
}