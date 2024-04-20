#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main()
{
  pid_t pid;
  int i, sum = 0;
  pid = fork(); // fork! -> create a child process
  if (pid > 0)
  { // Run by the parent
    printf("Parent: fork()'s return == Child pid = %d\n", pid);
    printf("Parent: pid = %d\n", getpid());

    wait(NULL); // Wait for the child
    printf("Parent has been finished\n");
    return 0;
  }
  else if (pid == 0)
  { // Run by the child
    printf("\t-Child: fork()'s return pid = %d\n", pid);
    printf("\t-Child: pid = %d, parent's pid = %d\n", getpid(), getppid());

    for (i = 1; i <= 100; i++)
      sum += i;

    printf("\t-Child: sum = %d\n", sum);
    return 0;
  }
  else
  { // Error
    printf("fork error");
    return 0;
  }
  return 0;
}
