package com.company;
import java.util.Scanner;

public class Omkar_6_percentage_calculator {
    public static void main(String[] args) {
        System.out.println("CBSC percentage calculator");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter First Subject Marks");
        float a = sc.nextFloat();
        System.out.println("Enter Second Subject Marks");
        float b = sc.nextFloat();
        System.out.println("Enter Third Subject Marks");
        float c = sc.nextFloat();
        System.out.println("Enter Fourth Subject Marks");
        float d = sc.nextFloat();
        System.out.println("Enter Fifth Subject Marks");
        float e = sc.nextFloat();
        System.out.print("Total marks are : ");
        float total = (a+b+c+d+e);
        System.out.println(total);
        System.out.print("Percentage is : ");
        float percentage = total/5;
        System.out.println(percentage);
    }
}
