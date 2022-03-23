// Theme: switch문
#include <stdio.h>

int main() {
  int a, b;
  char op;

  printf("수식을 입력하세요 : ");
  scanf("%d %c %d", &a, &op, &b);

  switch (op) {
  case '+':
    printf("%d + %d = %d\n", a, b, a+b);
    break;
  case '-':
    printf("%d - %d = %d\n", a, b, a-b);
    break;
  case '*':
    printf("%d * %d = %d\n", a, b, a*b);
    break;
  case '/':
    printf("%d / %d = %d\n", a, b, a/b);
    break;
  default:
    printf("계산할 수 없습니다.\n");
    break;
  }
}