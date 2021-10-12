#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <sys/types.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <pthread.h>
#include <stdint.h>
#include <stdbool.h>
#include <semaphore.h>

#define  NOT_READY  -1
#define  FILLED     0
#define  TAKEN      1

sem_t 		mutex;
char 		buf[10];

struct Memory {
	uint32_t 	number;
	int  		slot[10]; //uint32_t
	int  		clientflag;
	int 		serverflag[10];
	int 		command;
};
