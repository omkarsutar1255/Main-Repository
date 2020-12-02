package com.company;

public class O10_Datatypes_Increament_Decreament {
    public static void main(String[] args) {
        // Datatypes of arithmetic operation
        int i = 456123789;
        byte b = 46;
        short s = 4562;
        long l = 1234654874545235429L;
        float f = 756.16f;
        double d = 5421.5446;
        char c = 'a';

        int sum1 = b + s;     // bytes + short = integer
        int sum2 = s + i;     // short + int = integer
        float sum3 = l + f;     // long + float = float
        float sum4 = i + f;     // int + float = float
        int sum5 = c + i;     // char + int = integer
        int sum6 = c + s;     // char + short = integer
        double sum7 = l + d;     // long + double = double
        double sum8 = f + d;     // float + double = double
        System.out.println(sum5);
        System.out.println(sum6);

        double h = ++sum7;                  // we can assign increment values to any variable
        System.out.println(sum1++);         // this print sum1 first then increment for future use
        System.out.println(sum1);           // now value is sum1 is incremented
        System.out.println(++sum2);         // this increment sum1 first then print

        double j = --sum8;                 // we can decrement values using -- sign to it
        double p = --sum8 * 8;             // we can use increment and decrement signs in evaluation
        System.out.println(p);

        char ch = 'B';
        System.out.println(++ch);      // this will increment B to C then use it
    }
}
