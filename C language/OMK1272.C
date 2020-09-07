#include<stdio.h>
#include<conio.h>
void main()
{
int n1=0,n2=1,n3,n;
clrscr();
printf("enter fibonacci number\n");
scanf("%d",&n);
printf("\n%d\n%d\n",n1,n2);
n = n-2;
while (n)
{
	n3=n1+n2;
	printf("%d\n",n3);
	n1=n2;
	n2=n3;
	n=n-1;
}
getch();
}

