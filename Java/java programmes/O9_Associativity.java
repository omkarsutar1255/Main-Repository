package com.company;

public class O9_Associativity {
    public static void main(String[] args) {
        int a = 3;
        int b = 4;
        int c = 5;
        int k = b*b - 4*a*c/(2*a);
        // java works on precedence & association rule for calculation
        System.out.println(k);
    }
}
