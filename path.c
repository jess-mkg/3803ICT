#include "include.h"

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
