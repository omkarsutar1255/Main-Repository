#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
 {
 clrscr();
 int a,b=1,d,e;
  while(b<=500)
   {
      a=b,e=0;
      while(a)
      {
      d=a%10;
	e=e+pow(d,3);
	a=a/10;
       }
       if(b==e)
      {
      printf("%d is armstrong\n",b);
      }
      b++ ;
   }
getch();
}