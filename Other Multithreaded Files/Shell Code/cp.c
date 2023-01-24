#include "include.h"

void copyFile(char *filename1, char *filename2) 
{
    FILE *source, *target;
    source = fopen(filename1, "r");
    if (source == NULL)
    {
        printf("Source file does not exist or could not be accessed ...\n");
    }
    else
    {
        char ch;
        target = fopen(filename2, "W");
        if (target == NULL)
        {
            printf("Target file does not exist or could not be accessed ...\n");
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