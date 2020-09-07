#include<stdio.h>
#include<conio.h>
void main()
{
 int n,r,a,i;
 clrscr();
 printf("Enter number and range :");
 scanf("%d%d",&n,&r);
 for(i=1; i<=r; i++)
     {
      a=n*i;

	printf("%d * %d = %d\n",n,i,a);
      }

 getch();
}