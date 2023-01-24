#include "include.h"

/* this file contains a function to display the current cwd path*/

void Path()
{
	char cwd[PATH_MAX];
	if (getcwd(cwd, sizeof(cwd)) != NULL)
	{
		printf("%s\n", cwd);
	}
	else
	{
		perror("Error! ... \n");
		/*return 1; */
	}
	/*return 0;*/
}
