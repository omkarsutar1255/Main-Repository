#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int a,b,c;
 printf("enter three number");
 scanf("%d%d%d",&a,&b,&c);

if (a>b)
{
 if(a>c)
 printf("%d is larger number",a);
 else
 printf("%d is the larger number",c);
}
else
{
 if(b>c)
 printf("%d is larger number",b);
 else
 printf("%d is larger number",c);
}
getch();
}











