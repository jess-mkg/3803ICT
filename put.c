#include <sys/stat.h>
#include <sys/types.h>
#include <stdio.h>
#include <errno.h>
#include <dirent.h>

void putFiles(const char *dirname)
{
	DIR *dir = opendir(dirname);
	if (dir) 
	{
		printf("Directory already exists ...\n");
		closedir(dir);
	}	
	else if (ENOENT == errno)
	{
		printf("Directory does not exist ...\n");
		mkdir(dirname, 0777);
	}
	else
	{
		printf("Error ...\n");
	}
}

