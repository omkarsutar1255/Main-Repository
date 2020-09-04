package com.company;
import java.util.Scanner;

public class Omkar_5_Getting_user_Input {
    public static void main(String[] args) {        // write main and enter
        System.out.println("It Works");             // write sout and enter
        Scanner sc = new Scanner(System.in);         // System.in takes input from system
        System.out.println("Enter Number 1");
//        int a = sc.nextInt();                         // now entered number will come into variable a
        float a = sc.nextFloat();                       // for float we can set nextfloat
        System.out.println("Enter number 2");
//        int b = sc.nextInt();                       // now entered number will be in b
        float b = sc.nextFloat();
//        int sum = a + b;
        float sum = a + b;
        System.out.println("The sum of these number is : ");
        System.out.println(sum);
        boolean b1 = sc.hasNextInt();                // hasnextint check input is integer or not
        System.out.println(b1);
//        String str = sc.next();                       // scan first word from string
        String str = sc.nextLine();                     // scan full string line
        System.out.println(str);
    }
}
