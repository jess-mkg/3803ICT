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

/*
     sem_unlink(SEM_READER_FNAME);
     sem_unlink(SEM_WRITER_FNAME);

     sem_t *sem_reader = sem_open(SEM_READER_FNAME, IPC_CREAT, 0666, 0);
     if (sem_reader == SEM_FAILED) {
         perror("sem_open/reader");
         exit(1);
     }

     sem_t *sem_writer = sem_open(SEM_WRITER_FNAME, IPC_CREAT, 0666, 1);
     if (sem_writer == SEM_FAILED) {
         perror("sem_open/writer");
         exit(1);
     }*/
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
             if (ShmPTR->command == "q") {
                 printf("   server has informed client data have been taken...\n");
                 ShmPTR->clientflag == 1;
                 shmdt((void *) ShmPTR);
                 printf("   server has detached its shared memory...\n");
                 printf("   server exits...\n");
                 exit(0);
             }
             else {
                 uint32_t new = ShmPTR->number;
                 for (int i = 0;i < 32; i++) {
                     uint32_t rotated = rotateRight(i, new);
                     printf("%d\n", rotated);
                 }

             }
             printf("testing value %d\n", ShmPTR->number);
         }
     }
     printf("   server has informed client data have been taken...\n");
     shmdt((void *) ShmPTR);
     printf("   server has detached its shared memory...\n");
     printf("   server exits...\n");
     exit(0);
}
