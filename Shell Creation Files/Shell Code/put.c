#include "include.h"
#define SIZE 25

/*This file contains a function to create a dir and copy files to it*/

void putFiles(const char *dirname, char *array[])
{
	DIR *dir = opendir(dirname);
	if (dir) 
	{
		printf("Directory already exists ...\n");
		closedir(dir);
	}	
	else if (ENOENT == errno)
	{
		mkdir(dirname);
		printf("Directory created ...\n");
	}
	else
	{
		printf("Error ...\n");
	}

	for (int i = 2; array[i] != NULL; i++)
	{	
		char *fulldir = malloc(SIZE*sizeof(char));
		FILE *source, *target; 
		source = fopen(array[i], "r");
		if (source == NULL)
		{
			printf("File '%s' does not exist here ...\n", array[i]);
		}
		else
		{	/*configuration of path name for file location*/
			char ch, *target_file;
			target_file = malloc(SIZE*sizeof(char));
			strcpy(target_file, dirname);
			strcat(target_file, "/");
			strcat(target_file, "copy_");
			strcat(target_file, array[i]);
			target = fopen(target_file, "w");
			if (target == NULL)
			{
				printf("File '%s' not created ... \n", target_file);
			}
			else
			{
				ch = fgetc(source);
				while (ch != EOF)
				{
					fputc(ch, target);
					ch = fgetc(source);
				}
				printf("File copied!\n");
			}
			fclose(target);
		}
		fclose(source);
	}
}

