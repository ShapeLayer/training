#include <stdio.h>

int main() {
  int pid = fork();
  if (!pid) {
    for (int i = 0; i < 4; i++) {
      fork();
    }
  } else {
    printf("pid: %d\n", pid);
  }
  return 0;
}