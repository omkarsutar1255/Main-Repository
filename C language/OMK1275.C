#include<stdio.h>
#include<conio.h>
void main()
{
   int a,b,i,p=1;
	clrscr();
   printf("enter two values");
   scanf("%d%d",&a,&b);
   for (i=1; i<=b; i++)
   {
	   p=a*p;

    }
    printf("%d is the power",p);

getch();
}