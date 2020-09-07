#include<stdio.h>
#include<conio.h>
void main()
{
	clrscr();
	int n,count,fact=1;
	printf("enter positive number");
	scanf("%d",&n);
	if (n==0)
	{
	   printf("The factorial of 0 is 1\n");
	}
	else
	{
		for (count=1; count<=n; count++)
		{
		    fact = fact * count;
		}
	}
	printf("the factrorial of %d is %d",n,fact);
	getch();
}