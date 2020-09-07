#include<stdio.h>
#include<conio.h>
main()
{
clrscr();
int a=5,b=10;
printf("before swapping");
printf("\na = %d",a);
printf(" b = %d",b);

a=a+b;
b=a-b;
a=a-b;
printf("\nafter swapping");
printf("\na = %d",a);
printf(" b = %d",b);
getch();
}