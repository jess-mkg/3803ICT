#define _GNU_SOURCE
#include "include.h"
#include <x86intrin.h>
#include <cpuid.h>
/* This file is called Sys.c - it contains instructions to
retrieve OS and CPU type name and version. */
void Sys()
{
	struct utsname uts;
	uname(&uts);
	/*
	int CPUInfo[4] = {-1};
	__cpuid(CPUInfo, 0x80000000);
	unsigned int nExIds = CPUInfo[0];
	unsigned int i;
	char CPUBrandString[0x40] = { 0 };
	for (i = 0x80000000; i <= nExIds; ++i)
	{	
		__cpuid(CPUInfo, i);
	
		if (i == 0x80000002)
		{
			memcpy(CPUBrandString,
			CPUInfo,
			sizeof(CPUInfo));
		}
		else if (i == 0x80000003)
		{
			memcpy(CPUBrandString + 16,
                	CPUInfo,
                	sizeof(CPUInfo));
		}
		else if (i == 0x80000004) 
        	{
               		memcpy(CPUBrandString + 32,
                	CPUInfo,
                	sizeof(CPUInfo));
        	}
	}*/ 
	/*
	FILE *cpuinfo =  fopen("/proc/cpuinfo", "rb");
	char *arg = 0;
	size_t size = 0;
	while(getdelim(&arg, &size, 0, cpuinfo) != -1)
	{
		puts(arg);
	}
	free(arg);
	fclose(cpuinfo);
	*/
	printf("OS name..............: %s\n", uts.sysname);
	printf("OS version...........: %s\n", uts.version);
	printf("CPU type name........: \n" /*CPUBrandString*/);
	printf("CPU type version.....: \n");
}
