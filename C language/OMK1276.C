#include<stdio.h>
#include<conio.h>
int main()
{
clrscr();
int a,b,c=0,temp;
printf("enter a number");
scanf("%d",&a);
temp = a;
while(a)
   {
	b=a%10;
	c=(c*10)+b;
	a=a/10;
}
printf("reverse of digits is %d\n",c);
if(c==temp)
  {
   printf("the entered number is palindrome");
 }
else
    {
	     printf("the entered number is not palindrome");
  }
getch();
}