#include "include.h"

/* This file contains a function to so simple, positive, calcuations */ 

void calc(int a, int b, char op)
{
	if (op == '+')
	{
		printf("result: %d\n", (a + b));
	}
	else if (op == '-')
	{
		printf("result: %d\n", (a - b));
	}
	else
	{
		printf("Invalid statement ...\n");
	}
}
