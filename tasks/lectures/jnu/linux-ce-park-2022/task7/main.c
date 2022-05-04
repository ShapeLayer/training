#include <stdio.h>

int main() {
  for (int i = 0; i < 5; i++) {
    int pid = fork();
    if (pid == 0) {
      printf("pid: %d\n", getpid());
      exit(0);
    }
  }
  return 0;
}