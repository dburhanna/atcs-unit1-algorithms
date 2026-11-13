import java.util.*;

public class TreeCollectionsJava {
    public static void main(String[] args) {
        Set<Integer> values = new TreeSet<>();

        values.add(50);
        values.add(25);
        values.add(75);
        values.add(10);
        values.add(35);

        System.out.println(values);
        System.out.println(values.contains(35));
    }
}
