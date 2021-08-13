#include "include.h"

void calc(int a, int b, char op)
{
	if (op == '+')
	{
		printf("%d\n", a + b);
	}
	else if (op == '-')
	{
		printf("%d\n", a - b);
	}
	else
	{
		printf("Invalid statement ...\n");
	}
}
