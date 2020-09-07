#include<stdio.h>
#include<conio.h>
void main()
{
 clrscr();
  int a[2][3],i,j,total=0;
  printf("Enter 6 number\n");
 for(i=0; i<2; i++)
      {
	for(j=0; j<3; j++)
       {
	 scanf("%d",&a[i][j]);
	  total=total+a[i][j];
	}
      }
printf("total is %d",total);
getch();
 }