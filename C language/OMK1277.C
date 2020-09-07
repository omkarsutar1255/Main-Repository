#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
clrscr();
int a,b,c=0,temp;
printf("Enter the number");
scanf("%d",&a);
temp = a;
while(a)
 {
    b=a%10;
    c=pow(b,3)+c;
    a= a/10;
 }
 (c==temp)?(printf("the entered number is arm")):(printf("the entered number is not arm"));
getch();
}