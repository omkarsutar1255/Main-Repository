#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
int num,row=1,start;
printf("Enter number of row\n");
scanf("%d",num);
printf("\n");
while(row<=num)
  {
   start=1;
      while(start<=row)
	 {
	    printf("%c",(row+64));
	   start++;
	  }
       printf("\n");
      row++;
  }
getch();
}
