#include <stdio.h>

int main() {
  double a, b;
  printf("�� ���� �Է��ϼ��� : ");
  scanf("%Lf %Lf", &a, &b);
  double res = a / b;
  int res_int = a / b;
  if (res != (double)(res_int)) printf("��: %f", res);
  else printf("��: %d", res_int);
}
