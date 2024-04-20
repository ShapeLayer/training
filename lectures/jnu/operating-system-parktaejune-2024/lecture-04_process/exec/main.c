#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
  int pid;

  pid = fork();

  if (pid < 0) {
    printf("error");
    return -1;
  } else if (pid == 0) {
    execlp("echo", "", NULL);
    return 0;
  } else {
    wait(NULL);
    printf("child proc terminated\n");
    return 0;
  }
  return 0;
}
