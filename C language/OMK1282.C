#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int amount,a,b,c;
 printf("Enter amount\n");
 scanf("%d",&amount);
 a= amount/2000;
  b=amount%2000;
  c=a*2000;
 printf("%d *2000=%d\n",a,c);
  amount=b;
  a= amount/500;
  b=amount%500;
  c=a*500;
 printf("%d *500=%d\n",a,c);
  amount=b;
  a= amount/200;
  b=amount%200;
  c=a*200;
 printf("%d *200=%d\n",a,c);
  amount=b;
  a= amount/100;
  b=amount%100;
  c=a*100;
 printf("%d *100=%d\n",a,c);
  amount=b;
  a= amount/50;
  b=amount%50;
  c=a*50;
 printf("%d *50=%d\n",a,c);
  amount=b;
  a= amount/20;
  b=amount%20;
  c=a*20;
 printf("%d *20=%d\n",a,c);
  amount=b;
  a= amount/10;
  b=amount%10;
  c=a*10;
 printf("%d *10=%d\n",a,c);
  amount=b;
  a= amount/5;
  b=amount%5;
  c=a*5;
 printf("%d *5=%d\n",a,c);
  amount=b;
  a= amount/2;
  b=amount%2;
  c=a*2;
 printf("%d *2=%d\n",a,c);
  amount=b;
  a= amount/1;
  b=amount%1;
  c=a*1;
 printf("%d *1=%d\n",a,c);
getch();
}