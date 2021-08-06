#include <stdio.h>
#include <time.h> 

/*this function produces the local time and date of that moment*/

void TimeDate() 
{
	time_t current;
	time(&current);
	printf("%s", ctime(&current));
}
