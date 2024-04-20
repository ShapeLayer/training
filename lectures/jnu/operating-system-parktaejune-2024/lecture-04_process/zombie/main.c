#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main()
{
  pid_t pid, zompid;
  int status;

  pid = fork();
  if (pid > 0)
  {                         // parent's code
    sleep(10);              // sleep for sec
    zompid = wait(&status); // wait for the child
    printf("Parent: child %d has been finished with %d\n",
           zompid, WEXITSTATUS(status));
    return 0;
  }
  else if (pid == 0)
  { // child's code
    printf("Child: I am done %d \n", getpid());
    exit(100); // exit code 100
  }
  else
  {
    printf("fork error\n");
    return 0;
  }
}
