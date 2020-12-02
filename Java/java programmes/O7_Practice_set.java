package com.company;

import java.util.Scanner;

public class O7_Practice_set {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // Question 1 : printing name on screen
        System.out.println("Enter your name");
        String name = sc.next();
        System.out.println("Hello Welcome " + name + " to Java programme");  // concatenate string value with string
        // Question 2 : converting miles to kilometers
        System.out.println("Enter miles");
        double mile = sc.nextDouble();                // Float takes and give value up to 7 numbers
        double km = mile/0.621371;                    // Double takes and give value up to 16 numbers
        System.out.println("Total Kilogram is " + km);
        // Question 3 : check number is integer or not
        System.out.println("Enter Integer");
        System.out.println(sc.hasNextInt() + " integer number");       // directly paste hasnext function in sout
    }
}
