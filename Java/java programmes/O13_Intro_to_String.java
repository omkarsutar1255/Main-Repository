package com.company;
import java.util.Scanner;
public class O13_Intro_to_String {
    public static void main(String[] args) {
//        String name = new String("Omkar");
        String name = "Omkar";                     // Supports directly create string object
        System.out.println(name);                  // we cannot change string values directly bt
                                                   // can make copy of it then change in that copy
        int a = 6;
        float b = 5.667f;
        System.out.printf("the value of a if %d and value of b is %8.2f", a, b);
        // similar use as C language %d=int, %f=float, %c=char, %s=string
        // %.2f gives value upto 2 decimal point and %8.2f shows total 8 digit value
        System.out.println("");
        System.out.format("the value of a if %d and value of b is %f", a, b);
        // same use as printf do
        Scanner sc = new Scanner(System.in);
        String C = sc.nextLine();
        System.out.println(C);
    }
}
