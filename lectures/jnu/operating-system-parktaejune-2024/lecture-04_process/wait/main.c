#include <stdio.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int main()
{
  pid_t pid;
  int status;

  pid = fork();

  if (pid > 0)
  {
    printf("Parent: Wating for the child\n");
    wait(&status); // Wait.
    printf("Parent: child's exit code=%d\n", WEXITSTATUS(status));
    return 0;
  }
  else if (pid == 0)
  {
    execlp("/bin/ls", "ls", NULL); // run ls on the child
  }
  else
  {
    printf("fork error!");
    return 0;
  }
}