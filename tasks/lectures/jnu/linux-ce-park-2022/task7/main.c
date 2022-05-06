#include <stdio.h>

int main() {
  int pid = fork();
  /*
  for (int i = 0; i < 4; i++) {
    int pid = fork();
    if (pid == 0) {
      printf("pid: %d\n", getpid());
      exit(0);
    }
  }*/
  if (pid > 0) {
    printf("pid: %d\n", getpid());
    for (int i = 0; i < 4; i++) {
      pid = fork();
      printf("pid: %d\n", getpid());
    }
  }
  return 0;
}