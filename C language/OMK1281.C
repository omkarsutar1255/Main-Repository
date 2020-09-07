#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
 int a,b,c,f;
 printf("Enter three sides of triangles");
 scanf("%d%d%d",&a,&b,&c);
 if(a>b && a>c)
    f  = ((b+c)>a);
  else if (b>c)
	f = ((a+c)>b);
  else
	 f = ((a+b)>c);
if(f)
 printf("this is valid triangle");
 else
  printf("this is not valid triangle");
getch();
}