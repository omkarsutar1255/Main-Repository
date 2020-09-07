#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int num,big=0,limit;
printf("Enter limit of number");
scanf("%d",&limit);
printf("enter limit is %d",limit);
  scanf("%d",&num);
  big=num;
  limit=limit-1;
  while(limit>0)
    {
    scanf("%d",&num);
    if (num>big)
	{
	  big=num;
	}
      limit--;
    }
printf("biggest number is %d",big);
getch();
}