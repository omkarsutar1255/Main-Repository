#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int a,b,c=0;
 printf("enter number");
 scanf("%d",&a);
 while(a)
 {
   b=a%10;
   c=c*10+b;
   a=a/10;
}
printf("the reverse is %d",c);
getch();
}
