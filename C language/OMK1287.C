#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
  int a,b=1,c,d;
printf("Enter number");
scanf("%d",a);
  while(b<=a)
    {
	c=1;
       while(c<=(a-b))
       {
	 printf(" ");
	 c++;
	}
	d=1;
	while(d<(2*b-1))
	{
	 printf("r");
	  d++;
	 }
	 printf("\n");
       b++;
    }
getch();
}