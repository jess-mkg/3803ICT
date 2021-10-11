#include <pthread.h>
#include <semaphore.h>
#include "shared_memory.h"


int main() {
    char           command[4];
    key_t          ShmKEY;
    int            ShmID;
    struct Memory  *ShmPTR;

    /////////////////////////////////////////////////////

    if ((ShmKEY = ftok(".", 'x')) == -1) {
        perror("ftok");
        exit(1);
    }
    /*  create the segment: */
    if ((ShmID = shmget(ShmKEY, sizeof(struct Memory), IPC_CREAT | 0666)) == -1) {
        perror("shmget");
        exit(1);
    }
    printf("Shared memory segment created...\n");

    /* attach to the segment to get a pointer to it: */
    ShmPTR = (struct Memory *) shmat(ShmID, NULL, 0);
    if ((int) ShmPTR == -1) {
         perror("shmat");
         exit(1);
    }
    ShmPTR->clientflag = 0;
    //ShmPTR->serverflag[10] = {0};
    printf("client has attached the shared memory...\n");
    //ShmPTR->clientflag = 0;
    printf("%d\n", ShmPTR->clientflag);
    /////////////////////////////////////////////////////
    while(1) {
        if (ShmPTR->clientflag == 0) {
            printf("Input value or 'q': ");
            scanf("%s", command);
            if (strcmp(command, "q") == 0) {
                ShmPTR->clientflag = 1;
                ShmPTR->command = 2;
                shmdt((void *) ShmPTR);
                printf("client has detached its shared memory...\n");
                shmctl(ShmID, IPC_RMID, NULL);
                printf("client has removed its shared memory...\n");
                printf("client exits...\n");
                exit(0);
            }
            else if (isdigit(command[0]) != 0) {
                uint32_t num = atoi(command);
                ShmPTR->clientflag = 1;
                ShmPTR->number = num;
                printf("client has filled %d into shared memory...\n", ShmPTR->number);
            }
            else {
                printf("Invalid Input ... \n");
            }
        }
        if (ShmPTR->serverflag[0] == 1) {
            printf("%d -- result\n", ShmPTR->slot[0]);

        }
    }
}
