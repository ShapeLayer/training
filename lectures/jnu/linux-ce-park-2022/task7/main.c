#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
  int pid = fork();
  for (int i = 0; i < 3; i++) {
    if (pid == 0) {
      pid = fork();
    }
  }
  int waiting_child_pid;
  wait(&waiting_child_pid);
  printf("pid: %d\n", getpid());
}