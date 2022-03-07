#include <stdio.h>

int main(void) {
  char gets_char;
  int gets_int;
  float gets_float;

  printf("문자를 입력하세요 : ");
  scanf("%c", &gets_char);

  printf("정수를 입력하세요 : ");
  scanf("%d", &gets_int);

  printf("실수를 입력하세요 : ");
  scanf("%f", &gets_float);

  printf("문자 = %c, 정수 = %d, 실수 = %f\n", gets_char, gets_int, gets_float);
}