package com.company;

public class O14_String_Methods {
    public static void main(String[] args) {
        String a = "Omkar";                        // one way of creating new string
        String name = new String("OMKAR");   // second way of creating new string
        System.out.println("original string : " + a);

        int value = name.length();                // find out length of string
        System.out.println("length of string : " + value);   // print value of length of string

        String lstring = name.toLowerCase();      // convert string into lowercase
        System.out.println("lower case : " + lstring);

        String ustring = a.toUpperCase();      // convert string into lowercase and assign it to new variable
        System.out.println("upper case : " + ustring);
        System.out.println(a.toUpperCase());    // we can directly change it to upper case
        System.out.println(a);                  // cant change original string

        String without_trim = "      Sutar     ";
        System.out.println("trimmed string : " + without_trim.trim());     // remove space from sides of string
        System.out.println(without_trim);                               // original string is immutable

        String newString = "Hi, my name is Omkar Sutar. I am a smart working engineer specialised in mechanical " +
                "engineering with overall CGPA of 8.1";
        System.out.println(newString.substring(9, 60));      // returns a substring from start index to end index.
        // start index included and end index is excluded

        System.out.println(newString.replace('a', 'i'));  // replace 'a' char to 'i' char in whole string
        System.out.println(newString.replace("ing", "ed"));
        // replace 'ing' string to 'ed' string in whole string
        System.out.println(newString.replace("r", "aaa"));
        // we can also replace one char with any string and vise versa

        System.out.println(name.startsWith("OM"));  // checks the start of string is with OM (its case sensitive)
        System.out.println(name.endsWith("AR"));  // checks the end of string is with OM (its case sensitive)

        System.out.println(name.charAt(2));    // show which character on index number 2 of string

        System.out.println(name.indexOf("KA"));  // shows on which index this character lies
        System.out.println(name.indexOf("KA", 1));     // shows on which index "KA character lies but checking exclude characters before 1 index
        // Returns -1 if not found
        String newS = "OmkarOmkarOmkar";
        System.out.println(newS.lastIndexOf("kar", 7));  // now its start counting from right to left from 7 index

        System.out.println(name.equals("OMKAR"));            // returns if name variable equals to "OMKAR"
        System.out.println(name.equalsIgnoreCase("Omkar"));    // ignore case sensitivity

        // Escape Sequences
        System.out.println("use \n for new line");
        System.out.println("use \t for tab");
        System.out.println("use \" to print double quote");
        System.out.println("use \\ to print backlash");
    }
}
