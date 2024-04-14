#include <stdio.h>

int main() {
  int height;
  printf("높이를 입력하세요 : ");
  scanf("%d", &height);
  for (int i = 1; i <= height; i++) {
    for (int j = 1; j <= i; j++) {
      printf("*");
    }
    printf("\n");
  }
  return 0;
}
