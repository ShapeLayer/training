#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void invoke_fork(int identifier) {
  pid_t pid = fork();
  if (pid > 0) {
    printf("Invoked creating new process from thread #%d", identifier);
    wait(NULL);
  } else {
    printf("Created new process from thread #%d", identifier);
    sleep(1);
    return;
  }
}

void invoke_exec() {
  execl("/bin/echo", "echo", "Executed echo using execl", (char *)0);
}

void *thread_handler(int identifier) {
  if (identifier == 1) {
    sleep(4);
  } else if (identifier == 2) {
    invoke_fork(identifier);
    sleep(1);
    invoke_exec();
  }
  printf("Invoked creating new thread as thread #%d", identifier);
}

int main() {
  pthread_t tid[3];
  pthread_create(&tid[0], NULL, thread_handler, 0);
  pthread_create(&tid[1], NULL, thread_handler, 1);
  pthread_create(&tid[2], NULL, thread_handler, 2);
  return 0;
}
