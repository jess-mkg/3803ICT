#include "include.h"

int main()
{
	printf("Welcome to the shell... \n\n");
	printf("          __           __ __ \n");
	printf("   _____ / /__  ____  / // / \n");
	printf("  / ___// __  // _  // // / \n");
	printf(" (__  )/ / / //  __// // / \n");
	printf("/____//_/ /_//____//_//_/ \n\n\n");

	int end = 0;
	while (end != 1)
	{	
		char command[100];	
		printf("> ");
		fgets(command,100,stdin);
		char *pch;
		pch = strtok(command," ,-");
		int i = 0;
		char *arg[100];
		while(pch != NULL)
		{
			arg[i++] = pch;
			pch = strtok(NULL, " ,-");
		}
		char *cmp = arg[0];
		if ((strcmp(cmp, "quit\n") == 0) || (strcmp(cmp, "quit") == 0))
		{
			printf("Goodbye! ... \n");
			exit(1);
			end = 1;
		}
		else if ((strcmp(cmp, "time\n") == 0) || (strcmp(cmp, "time") == 0))
		{
			TimeDate();
		}
		else if ((strcmp(cmp, "path\n") == 0) || (strcmp(cmp, "path") == 0))
		{
			Path();
		}
		else if ((strcmp(cmp, "sys\n") == 0) || (strcmp(cmp, "sys") == 0))
		{
			Sys();
		}
		else if ((strcmp(cmp, "get\n") == 0) || (strcmp(cmp, "get") == 0))
		{	
			getFile(arg[1]);
		}
		else if ((strcmp(cmp, "put\n") == 0) || (strcmp(cmp, "put") == 0))	
		{	
			putFiles(arg[1],arg);
		}
		else if ((strcmp(cmp, "calc\n") == 0) || (strcmp(cmp, "calc") == 0))
		{
			int a = atoi(arg[1]);
			int b = atoi(arg[3]);
			char *op = arg[2];
			calc(a,b,*op);
		}
	}
	return 0;
}
