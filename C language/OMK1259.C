#include<stdio.h>
#include<conio.h>
 main()
{
clrscr();
int a=5,b=10,temp;
printf("before swapping");
printf("\na = %d",a);
printf(" b = %d",b);
temp=a;
a=b;
b=temp;
printf("\nafter swapping");
printf("\na = %d",a);
printf(" b = %d",b);

getch();
}