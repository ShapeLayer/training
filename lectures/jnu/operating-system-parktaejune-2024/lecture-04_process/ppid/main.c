#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
  pid_t pid, ppid;

  pid = getpid();   // get a PID
  ppid = getppid(); // get a Parent's PID

  printf("Process ID = %d, Parent's ID = %d\n", pid, ppid);
}
