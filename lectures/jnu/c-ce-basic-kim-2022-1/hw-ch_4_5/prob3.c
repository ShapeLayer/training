#include <stdio.h>

int main() {
  int gets, limits, i = 1;
  printf("���� ����� ����Ͻðڽ��ϱ�? : ");
  scanf("%d", &gets);
  printf("��� �ִ��� �Է��ϼ��� : ");
  scanf("%d", &limits);
  while (1) {
    if (gets * i > limits) break;
    printf("%d * %d = %d ", gets, i, gets*i);
    i++;
  }
  printf("\n");
  return 0;
}
