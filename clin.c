#include <pthread.h>
#include <semaphore.h>
#include "shared_memory.h"

key_t               ShmKEY;
int                 ShmID;
struct Memory       *ShmPTR;


void* nextInp() {
    int i;
    for (i = 0; i < 10; i++) {
        if (ShmPTR->serverflag[i] == 1) {
            printf("Query%d: %d \n", i, ShmPTR->slot[i]);
            ShmPTR->serverflag[i] = 0;
        }
        sleep(1);
    }
}

int main() {
    char           command[4];
    pthread_t      response;

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
    for (int d = 0; d < 10; d++) {
        ShmPTR->serverflag[d] = 0;
    }
    printf("client has attached the shared memory...\n");
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
        if (pthread_create(&response, NULL, &nextInp, NULL) != 0) {
            perror("Failed to create thread ...");
        }

        if (pthread_detach(response) != 0) {
            perror("Failed to join thread...");
        }
    }
    return 0;
}
