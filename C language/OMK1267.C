#include<stdio.h>
#include<math.h>
#include<conio.h>
void main()
{

	float a,b,c;
	float root1, root2;
	float r,root_part, denom;
	clrscr();
	printf("Enter values of a,b and c\n");
	scanf("%f%f%f", &a,&b,&c);

	r =((b*b)-(4*a*c));
	root_part=sqrt(r);
	denom     = 2 * a;
	root1 = (-b+root_part)/denom;
	root2 = (-b-root_part)/denom;
	printf("Root1 = %f\nRoot2 = %f", root1, root2);


	getch();

}