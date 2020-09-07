#include<stdio.h>
#include<conio.h>

int fact(int n)
  {
    if(n==0)
    return 0;
   else
     return n + fact(n-1);
  }
main()
{
 clrscr();
 int n;
 printf("Enter factorial number");
  scanf("%d",&n);
  printf("%d",fact(n));
 getch();
return 0;
}