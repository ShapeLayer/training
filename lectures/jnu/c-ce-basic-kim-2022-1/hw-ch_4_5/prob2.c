#include <stdio.h>

int main() {
  int height;
  printf("���̸� �Է��ϼ��� : ");
  scanf("%d", &height);
  for (int i = 1; i <= height; i++) {
    for (int j = 1; j <= i; j++) {
      printf("*");
    }
    printf("\n");
  }
  return 0;
}
