#include<stdio.h>
#include<conio.h>
void main()
{
clrscr();
int n;
printf("Enter year");
scanf("%d",&n);
if (n%4==0)
 printf("%d is leap year",n);
else
printf ("%d is not leap year");
getch();
}
