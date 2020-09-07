#include<stdio.h>
#include<conio.h>
void main()
{
clrscr();
int a,b,c,d;

printf ("first value");
scanf ("%d",&a);
printf ("whats the second value");
scanf("%d",&b);
printf("whats third");
scanf ("%d",&c);
printf ("last value");
scanf ("%d",&d);
 int l=a*b+(c+d);
printf ("the result is : %d",l);
getch ();
}