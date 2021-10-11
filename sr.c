#include "shared_memory.h"
#include <semaphore.h>

int rotateRight(int k) {
    return (k >> 1)|(k << 32-1);
}

void  main(void)
{
     key_t          ShmKEY;
     int            ShmID;
     struct Memory  *ShmPTR;


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
     }
     /////////////////////////////////////////////////////////////////
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
     /////////////////////////////////////////////////////////////////

     while (ShmPTR->status != FILLED) {
         printf("Server found the data is ready...\n");
         printf("Server found %d in shared memory...\n", ShmPTR->data[0]);

         if (ShmPTR->clientflag == "q") {
             printf("   server has informed client data have been taken...\n");
             shmdt((void *) ShmPTR);
             printf("   server has detached its shared memory...\n");
             printf("   server exits...\n");
             exit(0);
         }
         int k = ShmPTR->data[0];
         for (int i = 0; i < 32; i++) {
             int r = (k >> i)|(k << 32-i);
             printf("%d: %d\n", i+1, r);
         }

     }

     ShmPTR->status = TAKEN;
     printf("   server has informed client data have been taken...\n");
     shmdt((void *) ShmPTR);
     printf("   server has detached its shared memory...\n");
     printf("   server exits...\n");
     exit(0);
}
