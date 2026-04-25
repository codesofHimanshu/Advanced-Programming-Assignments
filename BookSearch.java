//Write a Java program using ArrayList to store book titles.
//Add at least 5 books and search for books whose title contains a given word

import java.util.ArrayList;
import java.util.Scanner;

public class BookSearch {
    public static void main(String[] args) {

        // Create ArrayList to store book titles
        ArrayList<String> books = new ArrayList<>();

        // Add at least 5 books
        books.add("Java Programming Basics");
        books.add("Data Structures in C");
        books.add("Python for Beginners");
        books.add("Web Development with React");
        books.add("Cloud Computing Concepts");

        // Take input word to search
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a word to search in book titles: ");
        String word = sc.nextLine();

        System.out.println("\nBooks containing the word '" + word + "':");

        // Search books whose title contains the given word
        for (String title : books) {
            if (title.toLowerCase().contains(word.toLowerCase())) {
                System.out.println(title);
            }
        }

        sc.close();
    }
}
