#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int a[5],i,c,total=0;
 printf("Enter 5 number");

 for (i=0;i<5; i++)
    {
      scanf("%d",&a[i]);
      total=total+a[i];

    }
     printf("total is %d",total);
getch();
}