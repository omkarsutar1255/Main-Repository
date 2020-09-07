#include<stdio.h>
#include<conio.h>

int main()
{
clrscr();
int a,b,c,d;

printf("enter dividend : ");
scanf ("%d",&a);
printf("enter divisor : ");
scanf("%d",&b);
 c=a/b;
 d=a%b;
printf("quotient : %d\n",c);
printf("reminder : %d",d);
 getch();

}