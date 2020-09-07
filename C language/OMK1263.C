#include<stdio.h>
#include<conio.h>
 void main()
 {
 clrscr();
 char ch;
 printf("enter the alphabet :");
 scanf("%c",&ch);
 if (ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
	{
	printf("the alphabet is vowel");
	}
 else
 {
  printf("the alphabet is consonent");
	}
 getch();
 }