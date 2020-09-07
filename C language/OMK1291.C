#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int a,b,count;
 printf("Enter tow number");
 scanf("%d%d",&a,&b);
count=a;
while(count<=b)
{
   if(count%2==0)
      {
       printf("%d\n",count);
       }
   count++;
}
getch();
}
