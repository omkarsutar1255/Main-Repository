#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int a,b,c=1;
  printf("enter base and exponent");
  scanf("%d%d",&a,&b);

  while(b)
  {
     c=a*c;
    b--;
  }
 printf("%d is power of numbers",c);
getch();
}