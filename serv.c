#include "shared_memory.h"
#include <semaphore.h>
#include <limits.h>

static inline uint32_t rotateRight(unsigned int i, uint32_t k) {
    unsigned int c = i;
    const uint32_t mask = (CHAR_BIT*sizeof(k) - 1);
    c &= mask;
    return (k>>c) | (k<<( (-c)&mask ));
}

void  main(void)
{
     key_t          ShmKEY;
     int            ShmID;
     struct Memory  *ShmPTR;

     //////////////////////////////////////////////////
     ShmKEY = ftok(".", 'x');
     ShmID = shmget(ShmKEY, sizeof(struct Memory), 0666);
     if (ShmID < 0) {
          printf("*** shmget error (server) ***\n");
          exit(1);
     }
     printf("Server has received a shared memory ...\n");

     ShmPTR = (struct Memory *) shmat(ShmID, NULL, 0);
     if ((int) ShmPTR == -1) {
          printf("*** shmat error (server) ***\n");
          exit(1);
     }
     printf("Server has attached the shared memory...\n");
     /////////////////////////////////////////////////////
     printf("ready for input\n");


     while (1) {
         if (ShmPTR->clientflag == 1) {
             printf("Reading: num %d \n", ShmPTR->number);
             printf("Reading: cf %d \n", ShmPTR->clientflag);
             sleep(1);
             if (ShmPTR->command == 2) {
                 printf("   Client has detacted from memory...\n");
                 ShmPTR->clientflag == 1;
                 shmdt((void *) ShmPTR);
                 printf("   Server has detached its shared memory...\n");
                 printf("   Server exits...\n");
                 exit(0);
             }
             else {
                 uint32_t new = ShmPTR->number;
                 for (int i = 0;i < 32; i++) {
                     uint32_t rotated = rotateRight(i, new);
                     printf("%d\n", rotated);
                     //pthread_t user;
                     //pthread_create()
                     ShmPTR->clientflag = 0;
                 }

             }
         }
     }
     printf("   Client has detacted from memory...\n");
     shmdt((void *) ShmPTR);
     printf("   Server has detached its shared memory...\n");
     printf("   Server exits...\n");
     exit(0);
}
