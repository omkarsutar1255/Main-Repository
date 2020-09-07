#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int n,a,b,temp,f,h=0;
 printf("enter number");
 scanf("%d",&n);
 temp=n;
 while(n)
   {
   a =n%10;
    b=1;
    f= 1;
     while(b<=a)
     {
       f=f*b;
       b++;
     }
    printf("Factorial of %d is %d\n", a,f);
     h=h+f;
   n =n/10;
   }
   if(temp==h)
    {
       printf("%d is strong",temp);
     }
    else
   {
      printf("%d is not strong",temp);
   }
getch();
}