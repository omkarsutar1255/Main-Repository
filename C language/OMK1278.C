#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int a,b,c=1;
  printf("Enter two values");
  scanf("%d%d",&a,&b);
while(c<=a)
  {
    printf("%d\n",c);
       int d=1;
	 while(d<=b)
       {
	   printf("%d\n",d);
	  d++;
	 }
   c++;
 }
getch();
}