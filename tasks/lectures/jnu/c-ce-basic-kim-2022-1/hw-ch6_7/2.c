#include <stdio.h>
#define ARRAY_SIZE 10
#define swap(a,b) {int t = a; a = b; b = t;}

int main() {
  int gets[ARRAY_SIZE];
  for (int i = 0; i < 10; i++) scanf("%d", &gets[i]);
  for (int last = ARRAY_SIZE; last > 0; last--) {
    for (int bubble = 0; bubble < ARRAY_SIZE-1; bubble++) {
      int p = bubble+1;
      if (gets[bubble] < gets[p]) { swap(gets[bubble], gets[p]); }
    }
  }
  for (int i = 0; i < ARRAY_SIZE; i++) printf("%d ", gets[i]);
  printf("\n");
  printf("가장 큰 값: %d \n", gets[0]);
}

