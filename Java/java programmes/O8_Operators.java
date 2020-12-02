package com.company;

public class O8_Operators {
    public static void main(String[] args) {
        int a = 4;
        int b = 6 % a;     // Modulo operator
        // 4.8 % 1.1 >> Returns a decimal remainder
        System.out.println(b);
        int c = 9;
        c *= 3;                   // assignment operator
        System.out.println(c);
        System.out.println(64==6);          // comparator operator
        System.out.println(64>5 && 64>98);  // Logical operator
        System.out.println(64>5 || 64>98);

        // bitwise operator
        System.out.println(2&3);  //2 = 0010 and 3 = 0011 here for addition 0+1=0, 1+1=1 and 0+0=0
                                  // so 0010 + 0011 = 0010 = 2
    }
}
