#include "include.h"

/*print first 40 lines of a file if it exits*/

void getFile(char *filename)
{
	printf("%s\n", filename);
	filename = "test.txt";
	printf("%s\n", filename);
	FILE *file = fopen(filename, "r");
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
		if (n % 40 == 0)
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
