#include<stdio.h>
#include<conio.h>
void main()
{
clrscr();
int num, count, sum = 0;
printf("Enter a positive number\n");
scanf("%d",&num);
printf("\nNatural number from 1 to %d are :\n",num);
for (count = 1; count<=num; count++)
{
       printf("%d\n", count);
       sum = sum + count;
}
printf("\nsum of natural number %d are : %d\n", num, sum);
getch();
}
