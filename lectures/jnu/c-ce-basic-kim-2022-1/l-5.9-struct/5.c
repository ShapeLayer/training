#include <stdio.h>
#include <math.h>

typedef struct time {
  unsigned int sec : 6;
  unsigned int min : 6;
  unsigned int hour : 5;
} TIME;

int main() {
  struct time t1;
  printf("time 구조체의 크기 : %d\n", sizeof(TIME));

  t1.hour = 5;
  t1.min = 30;
  t1.hour = 70;
  
  printf("%02d:%02d:%02d\n", t1.hour, t1.min, t1.sec);

  return 0;
}