package com.company;
import java.util.Scanner;

public class O12_Practice_set_2 {

    public static void main(String[] args) {
        // question 1
        float a = 7f / 4 * 9 / 2;              // integer /integer = integer (7/4=1)
        System.out.println(a);
        float b = 7f/4 * 9/2;              // float/integer = float(7/4=1.8)
        System.out.println(b);
        // question 2
        char grade = 'B';
        grade = (char)(grade + 8);         // use char to forcefully insert another dtype into char
        System.out.println(grade);
        grade = (char)(grade - 8);         // retrieving original char value
        System.out.println(grade);
        // question 3
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number :");
        int l = sc.nextInt();
        System.out.println(l>8);       // return true if condition satisfy
        // question 4
        float v = 40f;
        int u = 30;
        int k = 20;
        int s = 10;
        float ans = (v*v-u*u)/(2*k*s);
        System.out.println(ans);
        // question 5
        float j = (56f*56-34*34)/(2*6*8);
        System.out.println(j);
    }
}
