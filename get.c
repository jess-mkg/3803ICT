#include "include.h"

/*this file contains a function to retrive the content from a 
file and print first 40 lines of a file if it exits*/

void getFile(char *filename)
{
	printf("%s\n", filename);
	filename = "test.txt";
	printf("%s\n", filename);
	FILE *file = fopen(filename, "r");		/*opens wanted file*/
	if (file != NULL)
	{
		printf("File opened...\n");
	}
	else
	{
		perror(filename);
	}
	char line[256];
	int n = 0;
	while (fgets(line, sizeof(line), file))
	{
		n++;
		printf("%s", line);
		if (n % 40 == 0)		/*controlls the printing od each set of 40 lines*/
		{
			printf("Continue printing (Y/N) ... ");
			char enter;
			/*enter = getchar();*/
			scanf("  %c", &enter);
			if (enter == 'N')
			{
				break;
			}
			if (enter == 'Y')
			{
				continue;
			}
		}
	}
	printf("Filed closed ...\n");
	fclose(file);
}
