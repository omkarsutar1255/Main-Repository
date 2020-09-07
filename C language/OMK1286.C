#include<stdio.h>
#include<conio.h>
void main()
{
  clrscr();
int a,b=0,c=0,d=1;
printf("enter decimal number");
scanf("%d",a);
   while(a)
    {
     b=a%2;
     c = c+ ( b*d );
    d=d*10;
    a=a/2;
   }
  printf("%d",c);
getch();
}