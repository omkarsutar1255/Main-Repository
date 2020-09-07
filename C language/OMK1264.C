#include<stdio.h>
#include<conio.h>
void main()
{
	clrscr();
	int a,b,c;
	printf("enter three number");
	scanf("%d%d%d",&a,&b,&c);

if (a>b && a>c)
	printf("%d is the larger number",a);
if (b>a && b>c)
	printf("%d is the larger number",b);
if (c>a && c>b)
	printf("%d is the larger number",c);
getch();
}