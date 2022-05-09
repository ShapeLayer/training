// Runs at AmazonLinux

#include <stdio.h>
#include <signal.h>
void intHandler();
/* 인터럽트 시그널을 처리한다. */
int main()
{
  signal(SIGINT, intHandler);
  for(;;) {	/* 무한 루틴 */
    printf("… processing …\n");
    sleep(10);
  }	/* for end */
  printf("실행되지 않음 \n");
}

void intHandler() {
  printf("\nKeyboardInterrupt Signal: %d\n", SIGINT);
}
