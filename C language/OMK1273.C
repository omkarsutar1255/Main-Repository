#include<stdio.h>
#include<conio.h>
void main()
{
int num1,num2,gcd,lcm,rem,numerator,denominator;
clrscr();
printf("Enter 2 interger numbers\n");
scanf("%d%d",&num1,&num2);
 if (num1 > num2)
   {
     numerator = num1;
     denominator = num2;
    }
 else
    {
       numerator = num2;
       denominator = num1;
}
rem = numerator % denominator;
while(rem!=0)
  {
   numerator = denominator;
   denominator = rem;
   rem = numerator%denominator;
 }
 gcd = denominator;
 lcm = (num1*num2)/gcd;
printf("GCD of %d and %d is %d\n", num1,num2,gcd);
printf("LCM of %d and %d is %d\n", num1,num2,lcm);
getch();
}