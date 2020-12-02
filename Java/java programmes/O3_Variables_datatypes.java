package com.company;             // group of java classes (usually company name)

public class O3_Variables_datatypes {              // classes in java

    public static void main(String[] args) {      // functions of classes and void means return nothing from function
                                    // public means we can access this function from anywhere
        // static allows us to run this function without making object
	// write your code here
        System.out.println("hello word");           // println set new line at end
        System.out.print("Sum of three number is : ");  // we can use print for same line
        int num1 = 78;                                  // define data type for variable
        int num2 = 566;
        int num3 = 45;
        int sum = num1 + num2 + num3;                   // adding three number
        System.out.print(sum);
    }
}
// Classes names are in PascalConvention i.e. FirstLetterOfEveryWordIsCapital
// functions names are in camelCaseConvention i.e. firstLetterOfFirstWordIsSmall (other words first letter should capital)

// primitive data types in java - int, long, double, short, byte, float, char, bool.
