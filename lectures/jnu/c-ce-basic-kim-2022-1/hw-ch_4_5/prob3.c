#include <stdio.h>

int main() {
  int gets, limits, i = 1;
  printf("몇의 배수를 출력하시겠습니까? : ");
  scanf("%d", &gets);
  printf("결과 최댓값을 입력하세요 : ");
  scanf("%d", &limits);
  while (1) {
    if (gets * i > limits) break;
    printf("%d * %d = %d ", gets, i, gets*i);
    i++;
  }
  printf("\n");
  return 0;
}
