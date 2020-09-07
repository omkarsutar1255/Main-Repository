 #include<stdio.h>
#include<conio.h>

 int sum(int num)
{
	if(num)
	return (num + sum(num-1));
	 else
	 return 0;

}

int main()
 {
  clrscr();
 int limit;
 printf("Enter the limit\n");
 scanf("%d",&limit);
 printf("sum of %d is %d",limit,sum(limit));
 getch();
 return 0;
}