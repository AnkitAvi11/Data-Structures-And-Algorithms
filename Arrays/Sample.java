
abstract class Fruit {
    protected String name, taste, size;

    public Fruit (String name, String taste, String size) {
        this.name = name;
        this.taste = taste;
        this.size = size;
    }

    abstract public void eat ();
}

class Apple extends Fruit {
    public Apple() {
        super("Apple", "taste like apple", "medium size");
    }

    public void eat() {
        System.out.println("I am eating " + this.name + " tastes like : " + this.taste + " whose size is : " + this.size);
    }

}

class Orange extends Fruit {
    public Orange() {
        super("Orange", "taste like orange", "lasrge size");
    }

    public void eat() {
        System.out.println("I am eating " + this.name + " tastes like : " + this.taste + " whose size is : " + this.size);
    }

}

class Sample {
    public static void main(String[] args) {
        Apple apple = new Apple();
        Orange orange = new Orange();
        apple.eat();
        orange.eat();
    }
}